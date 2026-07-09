# syntax=docker/dockerfile:1

# ---- Stage 1: install frontend deps with a modern npm (lockfileVersion 3) ----
FROM node:20-bookworm-slim AS frontend-deps
WORKDIR /repo/frontend
COPY frontend/package.json frontend/package-lock.json ./
# --ignore-scripts: node-sass's install/postinstall would try to fetch (or
# compile from source) a binary matched to this stage's Node 20 ABI, which
# we're about to throw away anyway -- the real rebuild for Node 14's ABI
# happens explicitly in the next stage.
RUN npm ci --legacy-peer-deps --ignore-scripts

# ---- Stage 2: build the frontend bundle with Node 14 (node-sass native ABI) ----
FROM node:14-buster-slim AS frontend-build
WORKDIR /repo/frontend
COPY --from=frontend-deps /repo/frontend/node_modules ./node_modules
# node-sass ships a prebuilt binary matched to the Node ABI it was installed
# under; since node_modules came from the Node 20 stage, refetch/rebuild the
# binary for Node 14 before running the actual build.
RUN node node_modules/node-sass/scripts/install.js && \
    node node_modules/node-sass/scripts/build.js
COPY frontend/ ./
RUN npm run build

# ---- Stage 3: backend runtime ----
FROM python:3.8-slim-bookworm AS backend
ENV PYTHONUNBUFFERED=1 \
    QT_QPA_PLATFORM=offscreen \
    DJANGO_SETTINGS_MODULE=config.settings.production

RUN apt-get update && apt-get install -y --no-install-recommends \
    musescore3 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /repo
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY backend/ backend/
# raw corpora, needed once to populate the persistent volume's db.sqlite3
# via `manage.py add_scores` (see datasets/README.md) -- not read at
# request time otherwise
COPY datasets/ datasets/
# built frontend assets land next to backend/, matching PROJECT_ROOT in
# backend/config/settings/base.py (one level above BACKEND_DIR)
COPY --from=frontend-build /repo/build ./build
COPY --from=frontend-build /repo/webpack-stats.json ./webpack-stats.json

# SECRET_KEY is only required by production.py's os.environ[...] lookup;
# collectstatic never uses its value, so a placeholder scoped to this one
# RUN is enough -- the real secret is injected at runtime via `fly secrets`.
RUN DJANGO_SECRET_KEY=build-time-placeholder python backend/manage.py collectstatic --noinput

COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

EXPOSE 8000
ENTRYPOINT ["/docker-entrypoint.sh"]

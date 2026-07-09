import React, { useState } from 'react';
import { Navbar, Footer } from '../UILibrary/components';
import Result from './Result';

const SOURCES = [
    { key: 'rs200_tdc', label: 'RS200 (Trevor de Clercq)' },
    { key: 'rs200_dt', label: 'RS200 (David Temperley)' },
    { key: 'mcgill_billboard', label: 'McGill Billboard' },
    { key: 'meta_pop', label: 'Meta-Corpus' },
];

function SearchView() {
    const [query, setQuery] = useState('');
    const [scores, setScores] = useState([]);
    const [info, setInfo] = useState({});
    const [selectedSources, setSelectedSources] = useState(SOURCES.map((s) => s.key));

    function toggleSource(key) {
        setSelectedSources((prev) => (
            prev.includes(key) ? prev.filter((k) => k !== key) : [...prev, key]
        ));
    }

    async function getResults() {
        const params = new URLSearchParams({ sources: selectedSources.join(',') });
        const json = await fetch(`/api/search/${query}?${params}`).then((res) => res.json());
        setScores(json.scores);
        setInfo({ found: json.found, hits: json.hits, total: json.total });
    }

    return (
        <React.Fragment>
            <Navbar />
            <main className="main container-fluid" style={{ maxWidth: '1200px', minHeight: '720px' }}>
                <div className="col-12 py-3">
                    <div>
                        <p> Search for scores in the database using Roman Numerals (e.g., I-V-vi-IV). The Roman Numerals are tonic-agnostic, based on the overall diatonic collections.</p>
                        <p> Current database includes <a href='https://rockcorpus.midside.com/harmonic_analyses.html'>RS Corpus</a>, <a href='https://ddmal.ca/research/The_McGill_Billboard_Project_(Chord_Analysis_Dataset)/'>The McGill Billboard Corpus</a>, and <a href='https://www.kaggle.com/datasets/jpmusdata/meta-corpus-complete-aggregate'>Meta-corpus</a>.</p>
                    </div>
                    <div style={{
                        display: 'flex', flexWrap: 'wrap', gap: '15px', marginBottom: '10px',
                    }}
                    >
                        {SOURCES.map(({ key, label }) => (
                            <label
                                key={key}
                                style={{
                                    display: 'flex', alignItems: 'center', gap: '5px', marginBottom: 0, fontWeight: 'normal',
                                }}
                            >
                                <input
                                    type="checkbox"
                                    checked={selectedSources.includes(key)}
                                    onChange={() => toggleSource(key)}
                                />
                                {label}
                            </label>
                        ))}
                    </div>
                    <div className="input-group">
                        <input
                            value={query}
                            onChange={(e) => setQuery(e.target.value)}
                            onKeyDown={(e) => { if (e.key === 'Enter') getResults(); }}
                            className="form-control"
                        />
                        <div className="input-group-append">
                            <button className="btn btn-primary" onClick={getResults}>
                                Search
                            </button>
                        </div>
                    </div>
                    <div className="card">
                        {scores.length === 0 ?
                            <div className="alert alert-secondary" style={{ margin: 0 }}> No results. </div>
                            :
                            <>
                                <div className="alert alert-success" style={{ margin: 0 }}>
                                    The progression was found in {info.found} of {info.total} scores for a total of {info.hits} times.
                                </div>
                                <ul className="list-group" style={{ maxHeight: '500px', overflow: 'auto' }}>
                                    {scores.map((score) => (
                                        <Result
                                            key={score.file}
                                            file={score.file}
                                            title={score.title}
                                            composer={score.composer}
                                            hits={score.hits}
                                            bySection={score.by_section}
                                        />
                                    ))}
                                </ul>
                            </>
                        }
                    </div>
                </div>
            </main>
            <Footer />
        </React.Fragment>
    );
}

export default SearchView;

import React, { useState } from 'react';
import PropTypes from 'prop-types';

function Result({
    file, title, composer, hits,
}) {
    const [open, setOpen] = useState(false);

    return (
        <li className="list-group-item">
            <div style={{ display: 'flex', alignItems: 'center' }}>
                <div
                    onClick={() => setOpen(!open)}
                    style={{ cursor: 'pointer' }}
                    title="Click to preview the score and see download options"
                >
                    <div style={{ textDecoration: 'underline' }}>{title || file}</div>
                    {composer && <small className="text-muted">{composer}</small>}
                </div>
                <span style={{ flex: 1 }}></span>
                {hits}
                <button
                    className="btn btn-outline-info"
                    style={{
                        marginLeft: '10px',
                        width: '40px'
                    }}
                    onClick={() => setOpen(!open)}
                >
                    {open ? '-' : '+'}
                </button>
            </div>
            {open &&
            <div>
                <div style={{ display: 'flex '}}>
                    downloads:
                    <span style={{ flex: 1 }}></span>
                    <a href={`api/score/${file}`}> score </a>
                    <a href={`api/score/text/${file}`} style={{ marginLeft: '10px' }}> original </a>
                    <a href={`api/score/facts/${file}`} style={{ marginLeft: '10px' }}> factsheet </a>
                </div>
                <div style={{ marginTop: '10px' }}>
                    <p className="text-muted" style={{ marginBottom: '5px' }}>
                        Rendering a preview may take up to 20 seconds the first time.
                    </p>
                    <embed
                        src={`/api/score/pdf/${file}`}
                        type="application/pdf"
                        width="100%"
                        height="600px"
                    />
                </div>
            </div>
            }
        </li>
    );
}

Result.propTypes = {
    file: PropTypes.string,
    title: PropTypes.string,
    composer: PropTypes.string,
    hits: PropTypes.number,
};

export default Result;

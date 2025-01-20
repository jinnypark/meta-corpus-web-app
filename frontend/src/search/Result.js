import React, { useState } from 'react';
import PropTypes from 'prop-types';

function Result({ file, hits }) {
    const [open, setOpen] = useState(false);

    return (
        <li className="list-group-item">
            <div style={{ display: 'flex', alignItems: 'center' }}>
                {file}
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
            </div>
            }
        </li>
    );
}

Result.propTypes = {
    file: PropTypes.string,
    hits: PropTypes.number,
};

export default Result;

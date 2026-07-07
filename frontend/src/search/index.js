import React, { useState } from 'react';
import { Navbar, Footer } from '../UILibrary/components';
import Result from './Result';

function SearchView() {
    const [query, setQuery] = useState('');
    const [scores, setScores] = useState([]);
    const [info, setInfo] = useState({});

    async function getResults() {
        const json = await fetch(`/api/search/${query}`).then((res) => res.json());
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

import React, { useState } from 'react';
import { Navbar, Footer } from '../UILibrary/components';

function ScoreView() {
    const [query, setQuery] = useState('');

    async function fetchScore() {
        if (query !== '') {
            document.getElementById('download').click();
        }
    }

    return (
        <React.Fragment>
            <Navbar />
            <main className="main container-fluid">
                <div className="col-12 py-3">
                    <div>
                        <h1>Score</h1>
                        <p> Search for scores in the database using Roman Numerals (e.g., I-V-vi-IV). The Roman Numerals are tonic-agnostic, based on the overall diatonic collections.</p>
                        <p> Current database includes <a href='https://rockcorpus.midside.com/harmonic_analyses.html'>RS Corpus</a>, <a href='https://ddmal.ca/research/The_McGill_Billboard_Project_(Chord_Analysis_Dataset)/'>The McGill Billboard Corpus</a>, and <a href='https://www.kaggle.com/datasets/jpmusdata/meta-corpus-complete-aggregate'>Meta-corpus</a>.</p>
                    </div>
                    <div>
                        <input
                            value={query}
                            onChange={(e) => setQuery(e.target.value)}
                        />
                        <button onClick={fetchScore}>
                            Search
                        </button>
                    </div>
                    <a href={`/api/score/${query}`} id="download"/>
                </div>
            </main>
            <Footer />
        </React.Fragment>
    );
}

export default ScoreView;

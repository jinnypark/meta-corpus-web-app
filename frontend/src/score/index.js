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
                        <p> Search for a score in the database </p>
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

import React, { useState } from 'react';
import axios from 'axios';
import './styles.css';

function App() {
    const [email, setEmail] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            await axios.post('/api/users', { email });
            alert('You have successfully subscribed for notifications!');
            setEmail('');
        } catch (error) {
            console.error(error);
            alert('Error subscribing for notifications.');
        }
    };

    return (
        <div className="App">
            <h1>Solar Energy Optimizer</h1>
            <form onSubmit={handleSubmit}>
                <input
                    type="email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    placeholder="Enter your email"
                    required
                />
                <button type="submit">Subscribe</button>
            </form>
        </div>
    );
}

export default App;
  
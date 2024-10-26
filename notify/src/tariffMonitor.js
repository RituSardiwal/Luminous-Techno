import React, { useEffect, useState } from 'react';

function TariffMonitor() {
    const [tariffs, setTariffs] = useState([]);
    const [error, setError] = useState(null);

    useEffect(() => {
        // Fetch data from the Flask API
        fetch("http://127.0.0.1:5000/api/tariff")
            .then(response => {
                if (!response.ok) {
                    throw new Error("Could not fetch tariff data");
                }
                return response.json();
            })
            .then(data => setTariffs(data))
            .catch(err => setError(err.message));
    }, []);

    // Extract the current and upcoming tariffs
    const currentTariff = tariffs[0];
    const upcomingTariffs = tariffs.slice(1, 4); // Show next 3 tariffs as upcoming

    return (
        <div style={styles.container}>
            <h2>Electricity Tariff Monitor</h2>
            {error && <p style={styles.error}>{error}</p>}
            {currentTariff ? (
                <>
                    <div style={styles.current}>
                        <h3>Current Price</h3>
                        <p>{new Date(currentTariff.timestamp).toLocaleString()} - ${currentTariff.price} / kWh</p>
                    </div>
                    <div style={styles.upcoming}>
                        <h3>Upcoming Prices</h3>
                        <ul style={styles.list}>
                            {upcomingTariffs.map((tariff, index) => (
                                <li key={index}>
                                    <strong>{new Date(tariff.timestamp).toLocaleString()}</strong>: ${tariff.price} / kWh
                                </li>
                            ))}
                        </ul>
                    </div>
                </>
            ) : (
                <p>Loading data...</p>
            )}
        </div>
    );
}

const styles = {
    container: {
        padding: '20px',
        fontFamily: 'Arial, sans-serif',
        maxWidth: '500px',
        margin: 'auto',
        backgroundColor: '#f9f9f9',
        borderRadius: '8px',
        boxShadow: '0 4px 8px rgba(0, 0, 0, 0.1)',
    },
    current: {
        marginBottom: '20px',
    },
    upcoming: {
        marginTop: '10px',
    },
    list: {
        listStyleType: 'none',
        padding: 0,
    },
    error: {
        color: 'red',
    }
};

export default TariffMonitor;

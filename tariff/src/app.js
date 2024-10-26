import React, { useEffect, useState } from 'react';

function App() {
  const [tariffs, setTariffs] = useState([]);

  useEffect(() => {
    fetch('/api/tariffs')
      .then((response) => response.json())
      .then((data) => setTariffs(data))
      .catch((error) => console.error('Error fetching tariff data:', error));
  }, []);

  return (
    <div>
      <h1>Real-Time Tariff Monitoring</h1>
      <table>
        <thead>
          <tr>
            <th>Date</th>
            <th>Solar Power (kW)</th>
            <th>Solar Energy Generation (kWh)</th>
            <th>Consumption Value (kW)</th>
          </tr>
        </thead>
        <tbody>
          {tariffs.map((tariff, index) => (
            <tr key={index}>
              <td>{new Date(tariff.SendDate).toLocaleString()}</td>
              <td>{tariff['Solar Power (kW)']}</td>
              <td>{tariff['Solar energy Generation (kWh)']}</td>
              <td>{tariff['consumptionValue (kW)']}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;

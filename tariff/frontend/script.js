document.addEventListener('DOMContentLoaded', () => {
    fetch('/api/tariffs')
        .then((response) => response.json())
        .then((data) => {
            const tableBody = document.getElementById('tariff-table').getElementsByTagName('tbody')[0];

            data.forEach((tariff) => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${new Date(tariff.SendDate).toLocaleString()}</td>
                    <td>${tariff['Solar Power (kW)']}</td>
                    <td>${tariff['Solar Energy Generation (kWh)']}</td>
                    <td>${tariff['Consumption Value (kW)']}</td>
                `;
                tableBody.appendChild(row);
            });
        })
        .catch((error) => console.error('Error fetching tariff data:', error));
});

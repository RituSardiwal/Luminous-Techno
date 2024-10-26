from flask import Flask, jsonify, request
from scheduler import schedule_appliances, initialize_scheduler
from utils import get_tariff_data  # Assuming utils has the tariff fetching function

app = Flask(__name__)

# Load initial tariffs and schedule appliances
initialize_scheduler()

@app.route('/fetch_tariff', methods=['GET'])
def fetch_tariff():
    """Fetch the latest tariff data."""
    # Use the actual function to get low-tariff period based on solar power data
    tariff_data = get_tariff_data()
    return jsonify(tariff_data), 200

@app.route('/schedule', methods=['POST'])
def schedule():
    """Manually trigger scheduling based on tariff data."""
    schedule_appliances()
    return jsonify({"status": "Scheduled appliances for low-tariff periods"}), 200

if __name__ == '__main__':
    app.run(port=5000, debug=True)

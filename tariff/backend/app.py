from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

# Load the CSV file with tariff data
data = pd.read_csv('energydata.csv', parse_dates=['SendDate'])

@app.route('/api/tariffs', methods=['GET'])
def get_tariffs():
    # Convert DataFrame to dictionary format for JSON response
    tariffs = data.to_dict(orient='records')
    return jsonify(tariffs)

if __name__ == '__main__':
    app.run(debug=True)


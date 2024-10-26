import csv
from datetime import datetime, timedelta

def get_tariff_data():
    """Determine low-tariff periods based on solar power or predefined schedule."""
    tariff_data = {}
    low_tariff_start = None
    low_tariff_end = None

    # Example threshold for low-tariff based on solar power
    threshold = 5.0  # kW, adjust this threshold based on your criteria

    with open('energydata.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        for row in csv_reader:
            solar_power = float(row['Solar Power (kW)'])
            send_date = datetime.strptime(row['SendDate'], "%m/%d/%Y %H:%M")  # Updated date format

            # Check if solar power exceeds threshold for low tariff
            if solar_power > threshold:
                if not low_tariff_start:
                    low_tariff_start = send_date
                low_tariff_end = send_date  # Update end time to the last matching row

        # Schedule appliances for the identified low-tariff period
        if low_tariff_start and low_tariff_end:
            tariff_data = {
                "time_period": f"{low_tariff_start.strftime('%H:%M')}-{low_tariff_end.strftime('%H:%M')}",
                "appliances": {
                    "washing_machine": {"start_time": low_tariff_start, "end_time": low_tariff_end},
                    "dishwasher": {"start_time": low_tariff_start + timedelta(minutes=30), "end_time": low_tariff_end},
                    "ev_charger": {"start_time": low_tariff_start + timedelta(minutes=60), "end_time": low_tariff_end}
                }
            }
    return tariff_data


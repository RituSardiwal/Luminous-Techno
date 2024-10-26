import pandas as pd
from datetime import datetime

def get_tariff_data():
    """Fetch tariff data from energydata.csv."""
    df = pd.read_csv('energydata.csv')
    
    # Convert the 'SendDate' column to datetime format
    df['SendDate'] = pd.to_datetime(df['SendDate'], format='%m/%d/%Y %H:%M')

    # Get the current time
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M')
    print(f"Current time for tariff check: {current_time}")

    # Attempt to find the current tariff
    current_tariff_data = df[df['SendDate'].dt.strftime('%Y-%m-%d %H:%M') == current_time]

    if current_tariff_data.empty:
        print("No matching tariff data found for the current time.")
        # Return default values or handle this case appropriately
        return {
            "current_tariff": 0,  # Default or error value
            "threshold_tariff": 0.15,
            "solar_energy_excess": False,
            "low_tariff_start": None
        }
    
    current_tariff = current_tariff_data['Solar Power (kW)'].values[0]

    # Determine if there's excess solar energy
    solar_energy_excess = df['Solar energy Generation (kWh)'].sum() > df['consumptionValue (kW)'].sum()

    return {
        "current_tariff": current_tariff,
        "threshold_tariff": 0.15,  # Update as necessary
        "solar_energy_excess": solar_energy_excess,
        "low_tariff_start": df['SendDate'].min()  # Example, you can customize this
    }

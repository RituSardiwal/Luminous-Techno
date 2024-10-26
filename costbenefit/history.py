import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Sample data generation
def generate_sample_data():
    data = {
        'SendDate': pd.date_range(start='2024-10-01', periods=24, freq='H'),
        'consumptionValue (kW)': np.random.uniform(0, 10, 24),  # Random consumption values
        'Solar Power (kW)': np.random.uniform(0, 10, 24),  # Random solar generation
        'tariff_rate (cents/kWh)': [15 if hour in range(8, 20) else 10 for hour in range(24)]  # 15 cents during peak hours
    }
    return pd.DataFrame(data)

# Function to calculate potential savings
def calculate_savings(df):
    savings_list = []
    for index, row in df.iterrows():
        peak_usage = min(row['consumptionValue (kW)'], row['Solar Power (kW)'])  # Solar energy offsets consumption
        if row['tariff_rate (cents/kWh)'] == 15:  # Peak rate
            savings = (row['consumptionValue (kW)'] * 15) - (peak_usage * 15)  # Savings from solar during peak
        else:  # Off-Peak rate
            savings = row['consumptionValue (kW)'] * 10  # Full cost during off-peak
        savings_list.append(savings)
    
    df['potential_savings (cents)'] = savings_list
    return df

# Function to display performance metrics
def display_performance_metrics(df):
    total_savings = df['potential_savings (cents)'].sum()
    average_savings = df['potential_savings (cents)'].mean()
    total_consumption = df['consumptionValue (kW)'].sum()
    total_solar_generation = df['Solar Power (kW)'].sum()
    
    print("Total Potential Savings: $", round(total_savings / 100, 2))  # Convert cents to dollars
    print("Average Savings per Hour: $", round(average_savings / 100, 2))
    print("Total Consumption: kWh", total_consumption)
    print("Total Solar Generation: kWh", total_solar_generation)

# Function to visualize savings over time
def visualize_savings(df):
    plt.figure(figsize=(12, 6))
    plt.plot(df['SendDate'], df['potential_savings (cents)'], marker='o', color='blue')
    plt.title('Potential Savings Over Time')
    plt.xlabel('Time')
    plt.ylabel('Potential Savings (cents)')
    plt.xticks(rotation=45)
    plt.grid()
    plt.tight_layout()
    plt.show()

# Main function to run the analysis
def main():
    # Generate sample data
    df = generate_sample_data()
    
    # Calculate potential savings
    df = calculate_savings(df)
    
    # Display performance metrics
    display_performance_metrics(df)
    
    # Visualize savings over time
    visualize_savings(df)

if __name__ == "__main__":
    main()

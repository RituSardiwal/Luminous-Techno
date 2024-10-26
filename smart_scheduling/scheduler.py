from utils import get_tariff_data

def schedule_appliances():
    """Schedule high-energy appliances for low-tariff periods."""
    tariff_data = get_tariff_data()  # Fetch low-tariff periods
    if not tariff_data:
        print("No low-tariff period available.")
        return

    appliances = tariff_data.get("appliances", {})
    for appliance, times in appliances.items():
        start_time = times["start_time"].strftime("%H:%M")
        end_time = times["end_time"].strftime("%H:%M")
        print(f"Scheduled {appliance} to run from {start_time} to {end_time}")

def initialize_scheduler():
    """Initialize and schedule appliances based on initial data."""
    print("Initializing scheduler...")
    schedule_appliances()


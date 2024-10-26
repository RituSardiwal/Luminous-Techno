import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from utils import get_tariff_data

def schedule_appliances(appliances_to_schedule):
    """Schedule specified appliances during low-tariff periods."""
    tariff_data = get_tariff_data()  # Fetch low-tariff periods
    
    # Apply custom scheduling based on the appliances in the JSON payload
    for appliance, duration in appliances_to_schedule.items():
        start_time = tariff_data["low_tariff_start"]
        end_time = start_time + timedelta(minutes=duration)
        print(f"Scheduled {appliance} from {start_time.strftime('%H:%M')} to {end_time.strftime('%H:%M')}")

def check_tariff_alerts():
    """Check for upcoming high-tariff periods and send notifications."""
    tariff_data = get_tariff_data()
    
    # Assuming the logic to determine high-tariff periods
    if tariff_data["current_tariff"] > tariff_data["threshold_tariff"]:
        send_email_notification("Upcoming high-tariff period!", "Consider using appliances during off-peak times.")
    
    # Check for excess solar energy opportunities
    if tariff_data["solar_energy_excess"]:
        send_email_notification("Sell Excess Solar Energy!", "You can sell your excess solar energy back to the grid.")

def send_email_notification(subject, message):
    """Send an email notification."""
    sender_email = "your_email@example.com"
    receiver_email = "user_email@example.com"
    password = "your_email_password"

    # Create the email content
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Add message body
    msg.attach(MIMEText(message, 'plain'))

    try:
        # Send the email
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.send_message(msg)
            print(f"Email sent: {subject}")
    except Exception as e:
        print(f"Failed to send email: {e}")

def initialize_scheduler():
    print("Initializing scheduler...")
    schedule_appliances({})

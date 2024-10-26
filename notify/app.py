from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from flask_cors import CORS
from apscheduler.schedulers.background import BackgroundScheduler
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///energy_data.db'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your_email@gmail.com'  # Your email
app.config['MAIL_PASSWORD'] = 'your_password'          # Your password
app.config['MAIL_DEFAULT_SENDER'] = 'your_email@gmail.com'  # Your email

db = SQLAlchemy(app)
CORS(app)
mail = Mail(app)

# Database models
class Tariff(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.Time)
    end_time = db.Column(db.Time)
    price = db.Column(db.Float)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    notified = db.Column(db.Boolean, default=False)

# Function to create tables
def create_tables():
    db.create_all()

# Function to check tariffs and send notifications
def check_tariffs_and_notify():
    threshold_price = 0.15  # Example threshold price for high tariff
    now = datetime.datetime.now().time()
    current_tariff = Tariff.query.filter(Tariff.start_time <= now, Tariff.end_time >= now).first()

    if current_tariff and current_tariff.price > threshold_price:
        users = User.query.filter_by(notified=False).all()
        for user in users:
            send_notification(user.email, current_tariff.price)
            user.notified = True  # Mark user as notified
            db.session.commit()

def send_notification(email, price):
    msg = Message('High Tariff Alert', recipients=[email])
    msg.body = f'The current electricity tariff is high: ${price} per kWh. Consider shifting your usage.'
    mail.send(msg)

# API route to add users
@app.route('/api/users', methods=['POST'])
def add_user():
    data = request.get_json()
    new_user = User(email=data['email'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User added!'}), 201

# API route to add tariffs
@app.route('/api/tariffs', methods=['POST'])
def add_tariff():
    data = request.get_json()
    new_tariff = Tariff(start_time=data['start_time'], end_time=data['end_time'], price=data['price'])
    db.session.add(new_tariff)
    db.session.commit()
    return jsonify({'message': 'Tariff added!'}), 201

# Homepage route
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    with app.app_context():
        create_tables()  # Create tables within the application context

    scheduler = BackgroundScheduler()
    scheduler.add_job(check_tariffs_and_notify, 'interval', minutes=10)  # Check every 10 minutes
    scheduler.start()
    app.run(debug=True)

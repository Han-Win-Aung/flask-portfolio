from flask import Flask
from flask_mail import Mail
import os

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('PORTFOLIO_EMAIL', 'hanwinag.dev@gmail.com')
app.config['MAIL_PASSWORD'] = os.environ.get('PORTFOLIO_EMAIL_PASSWORD', 'ribs ocyv pgbw hcwp')
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'Qw8v1n2p3r4s5t6u7v8w9x0y1z2A3B4C5D6E7F8G9H0I1J2')

mail = Mail(app)

from app import routes

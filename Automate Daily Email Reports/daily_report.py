import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime
import logging
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
# Load environment variables
smtp_host = os.getenv('SMTP_HOST')
smtp_port = int(os.getenv('SMTP_PORT'))
smtp_user = os.getenv('SMTP_USER')
smtp_password = os.getenv('SMTP_PASSWORD')

sender = os.getenv('SENDER_EMAIL')
receiver = os.getenv('RECEIVER_EMAIL')
subject = 'Daily Report - ' + datetime.date.today().strftime('%Y-%m-%d')

# Configure logging
logging.basicConfig(filename='daily_report.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

# Read email body template
with open('email_template.html', 'r') as file:
    body = file.read().format(date=datetime.date.today().strftime('%Y-%m-%d'))

# Create the email content
message = MIMEMultipart()
message['From'] = sender
message['To'] = receiver
message['Subject'] = subject
message.attach(MIMEText(body, 'html'))

# Connect to the SMTP server and send the email
try:
    smtp_server = smtplib.SMTP(smtp_host, smtp_port)
    smtp_server.starttls()
    smtp_server.login(smtp_user, smtp_password)
    smtp_server.sendmail(sender, receiver, message.as_string())
    smtp_server.quit()
    logging.info('Email sent successfully')
except Exception as e:
    logging.error(f'Failed to send email. Error: {str(e)}')
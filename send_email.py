import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from dotenv import load_dotenv
import os

# Load variables from .env file
load_dotenv()

# Access the app password using os.getenv()
gmail_app_password = os.getenv("GMAIL_APP_PASSWORD")

def send_email(subject , message , receiver_email):
    # Set up the email parameters
    sender_email = 'irfanrasheed273@gmail.com'
    # receiver_email = 'tve21cs062@cet.ac.in'
    # subject = 'Subject of the Email is blank'
    # message = 'Hello, this is the email content.'

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    # Connect to the SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    # Login to your email account
    server.login(sender_email, gmail_app_password)

    # Send the email
    server.sendmail(sender_email, receiver_email, msg.as_string())

    # Close the connection
    server.quit()

    print('Email sent successfully!')

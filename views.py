from app import app
from flask import render_template, redirect, request
from key import password
from email.mime.text import MIMEText
import smtplib
from models import Portfolio

@app.route('/')
def index():
    portfolio = Portfolio.query.all()
    return render_template('index.html',portfolio=portfolio)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get("name")
    email = request.form.get('email')
    message = request.form.get('message')
    email_body = f'''
    You have received an message from {name}
    with email address {email}
    <blockquote>
    {message}
    </blockquote>
    '''
    subject = f'Get in Touch from {name}'
    sender= 'therealakarexcel@gmail.com'
    recipient = 'developerexcela@gmail.com'
    
    # Create an email message
    msg = MIMEText(email_body, "html")
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = recipient
   
    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(sender, password)
        smtp.sendmail(sender, recipient, msg.as_string())
        return redirect('/')
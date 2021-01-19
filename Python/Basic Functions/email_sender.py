from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
def email_sender(content):
    sender_email = 'SENDER EMAIL' 
    password = 'SENDER PASSWORD'
    dest_email = 'DESTINATION EMAIL'
    subject = 'SUBJECT'
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = dest_email
    msg.attach(MIMEText(content, 'html'))
    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()
    mail.login(sender_email, password)
    mail.sendmail(sender_email, dest_email, msg.as_string())
    mail.quit()
    print('Email sented!')
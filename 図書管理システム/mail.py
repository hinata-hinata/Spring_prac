import os
from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import random

def send_mail(to, subject, body):
    
    ID = 'h.ono.sys24@morijyobi.ac.jp'
    PASSWORD = os.environ['MAIL_PASS']
    HOST = 'smtp.gmail.com'
    PORT = 587
    
    msg = MIMEMultipart()

    msg.attach(MIMEText(body,'html'))
                    
    msg['Subject'] = subject     
    msg['From'] = ID  
    msg['To'] = to
     
    server = SMTP(HOST, PORT)
    server.starttls()
    server.login(ID, PASSWORD)
    
    server.send_message(msg)
    server.quit()
    
def auth_code():
    code = ''
    source = 'abcdefghijklmnopqrstuvwsyz1234567890'    
    for _ in range(5):
        code += random.choice(source)
    return code
 
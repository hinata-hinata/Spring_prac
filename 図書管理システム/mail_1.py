from mail import send_mail

to = input('to:')
subject = input('subject:')
body = input('body:')

send_mail(to, subject, body) 

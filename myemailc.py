#!/usr/bin/python3

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def mail_send(query):
    users = {'shiv':'shivsonic05@gmail.com','pranjal':'pranjal.alwar@gmail.com','subham':'subham.k.rai@gmail.com','anand':'anandrkskd@gmail.com','Gaurav':'gauravj9414@gmail.com'}
    email_user = 'your_email'
    email_password = 'your_password'
    email_send = users[query]

    subject = input("Subject: ")

    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email_send
    msg['Subject'] = subject

    body = input("Body: ")
    msg.attach(MIMEText(body,'plain'))

    text = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(email_user,email_password)


    server.sendmail(email_user,email_send,text)
    server.quit()

if __name__=="__main__":
    mail_send('shiv')


#import libraries 
import smtplib

to = input("Receiver address: ")
content = input("email body: \n")

def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("youremailaddress@gmail.com", "password")
    server.sendmail('youremailaddress@gmail.com',to, content)
    server.close()

sendEmail(to, content)

    
'''
Created on Apr 1, 2023

@author: hamit
'''
from lg.ILoger import ILogerr
import smtplib
from email.message import EmailMessage

class Maill(ILogerr):
    def logla(self, mesaj, evrak, DIZIN_BILGILERI):
        print('Connecting to Mail aT Database...' + mesaj)
        
    #msg = EmailMessage()
    #msg.set_content("Content")

# me == the sender's email address
# you == the recipient's email address
    #msg['Subject'] = ""
    #msg['From'] = "me"
    #msg['To'] = "you"

# Send the message via our own SMTP server.
    #s = smtplib.SMTP('localhost')
    #s.send_message(msg)
    #s.quit()

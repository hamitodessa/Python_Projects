'''
Created on Apr 1, 2023

@author: hamit
'''
from lg.lg_kayit.ILog_Kayit import ILogKayitInterface
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import  formatdate
from email.mime.base import MIMEBase
from email import encoders

class Maill(ILogKayitInterface):
    def logla(self, mesaj, evrak, DIZIN_BILGILERI):
        print('Connecting to Mail aT Database...' + mesaj)
        try:   
            smtp_server = 'mail.ukraine.com.ua'
            port = 587
            sender_email = 'info@plastbak.com.ua'
            password = 'CRy7lGgj'

            recipient_email = 'hamit@okumus.com'
            message = MIMEMultipart()
            message['Subject'] = 'Test E-Postası'
            message['From'] = sender_email
            message['To'] = recipient_email
            message['Date'] = formatdate(localtime=True)
            message.attach(MIMEText(mesaj))

            filename = "C:/OBS_SISTEM/" + os.getlogin() + "_OBS_SISTEM_2025.DB"
            part = MIMEBase('application', "octet-stream")
            part.set_payload(open(filename, "rb").read())
            encoders.encode_base64(part)

            part.add_header('Content-Disposition', 'attachment', filename=filename)
            message.attach(part)
            return
            print("burda")
            with smtplib.SMTP(smtp_server, port) as server:
                server.starttls()
                server.login(sender_email, password)
                server.sendmail(sender_email, recipient_email, message.as_string())
        except smtplib.SMTPAuthenticationError:
                print('Hata: Kimlik doğrulama başarısız oldu.')
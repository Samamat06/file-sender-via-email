import smtplib
import os

#cambio_dir
path = 'Directory where the file is'
os.chdir(path)

#variabili
lec = open("file_name", "r").read()

#codice
email = smtplib.SMTP("smtp.gmail.com", 587)
email.ehlo()
email.starttls()
email.login("our email", "email psw")
email.sendmail("sender email", "conferment email", lec)
email.quit()


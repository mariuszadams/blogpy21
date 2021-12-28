#!/usr/bin/env python
import smtplib,sys,os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

print ("running ", sys.argv[0]) # prints python_script.py
passwd= sys.argv[1]
fromaddr = "openshift@hub.pl"
toaddr = "kotestowy@interia.pl"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Openshift builder output from " +  str(sys.argv[0])
envar = "\n" + str(os.environ)

#Next, we attach the body of the email to the MIME message:
body = "Python test mail\n" + str(envar)
msg.attach(MIMEText(body, 'plain'))

print ("connecting to SMTP...")
server = smtplib.SMTP('poczta.interia.pl', 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login(fromaddr, passwd)
text = msg.as_string()

print ("sending ", msg['Subject'])
server.sendmail(fromaddr, toaddr, text)

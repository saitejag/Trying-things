import smtplib
server = smtplib.SMTP('smtp.gmail.com',587)
server.login("saitejag1502@gmail.com","")
msg = "Hello!"
server.sendmail("saitejag1502@gmail.com","lelouch1729@gmail.com",msg)

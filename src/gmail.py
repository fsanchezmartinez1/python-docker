from correo.mime.multipart import MIMEMultipart
from correo.mime.text import MIMEText
import smtplib
# create message object instance 
msg = MIMEMultipart()
message = "Thank you"
# setup the parameters of the message 
password = "password"
msg['From'] = "from@email.com"
msg['To'] = "to@email.com"
msg['Subject'] = "Subscription"
# add in the message body 
msg.attach(MIMEText(message, 'plain'))
#create server 
server = smtplib.SMTP('smtp.gmail.com: 587')
server.starttls()
# Login Credentials for sending the mail 
server.login(msg['From'], password)
# send the message via the server. 
server.sendmail(msg['From'], msg['To'], msg.as_string())
server.quit()
print("successfully sent email to %s:" % (msg['To']))
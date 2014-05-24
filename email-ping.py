import smtplib
import time
from email.mime.text import MIMEText

to_list = ('',)  # add recipient (your remote account) here
from_email = ''  # email from which the e-mail is sent; must be accepted by SMTP

s = smtplib.SMTP('')  # SMTP address
s.login('', '')  # ('smtp login', 'smtp password')

for to in to_list:
    msg = MIMEText('server status: OK')
    msg['Subject'] = 'Server status '+time.ctime()
    msg['From'] = from_email
    msg['To'] = to
    print msg.as_string()
    s.sendmail(from_email, [to], msg.as_string())


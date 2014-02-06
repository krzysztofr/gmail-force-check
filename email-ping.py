import smtplib, time
from email.mime.text import MIMEText

to_list = ('',)
from_email = ''

s = smtplib.SMTP('')
s.login('', '') # ('login', 'password')

msg = MIMEText('server status: OK')
msg['Subject'] = 'Server status '+time.ctime()
msg['From'] = from_email

for to in to_list:
    msg['To'] = to
    print msg.as_string()
    s.sendmail(from_email, [to], msg.as_string())


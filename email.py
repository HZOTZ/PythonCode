#!/usr/bin/env python
#-*-coding:utf-8-*-
 
import smtplib
from email.mime.text import MIMEText

MAIL_HOST = 'smtp.qq.com'
MAIL_PORT = '25'
MAIL_USERNAME = ''
MAIL_PASSWD = ''

server = smtplib.SMTP()
server.connect(MAIL_HOST,MAIL_PORT)
server.login(MAIL_USERNAME, MAIL_PASSWD)

msg = MIMEText(text.encode("utf-8") ,_subtype = text_type ,_charset = 'utf-8')
msg['Subject'] = subject.encode("utf-8")
me = "<" + from_ + ">"
msg['From'] = me
msg['To'] = ":" .join(to_list)

server.sendmail(from_, to_list, msg.as_string())
server.close()
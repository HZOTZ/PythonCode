#!/usr/bin/env python
#-*-coding:utf-8-*-

import smtplib
from email.mime.text import MIMEText

MAIL_HOST = 'smtp.qq.com'
MAIL_PORT = '25'
MAIL_USERNAME = ''
MAIL_PASSWD = ''

class MAIL(object):
	"""docstring for MAIL"""
	def __init__(self):
		pass

	def __enter__(self):
		self.server = smtplib.SMTP()
		self.server.connect(MAIL_HOST,MAIL_PORT)
		self.server.login(MAIL_USERNAME, MAIL_PASSWD)
		return self

	def _send_msg(self, from_, to_list, subject, text, text_type):
		msg = MIMEText(text.encode("utf-8") ,_subtype = text_type ,_charset = 'utf-8')
		msg['Subject'] = subject.encode("utf-8")
		me = "<" + from_ + ">"
		msg['From'] = me
		msg['To'] = ":" .join(to_list)		
		self.server.sendmail(from_, to_list, msg.as_string())

	def send_msg_text(self, from_, to_list, subject, text):
		self._send_msg(from_, to_list, subject, text, 'plain')

	def send_html(self, from_, to_list, subject, html):
		self._send_msg(from_, to_list, subject, html, 'html')

	def __exit__(self, exc_type, exc_value, exc_tb):
		self.server.close()
		return False

if __name__ == '__main__':
	with MAIL() as mail:
		mail.send_msg_text("1@1.com", #sender
			["2@2.com"], 				#receiver
			u"Hello Test 你好", 						#subject
			u"Good Test 好")							#msg

		mail.send_html("1@1.com", 
			["2@2.com"],
			 u"Hello Test 你好",
			 u"<a herf='http://www.163.com'>8错</a>")
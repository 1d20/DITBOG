#-*- coding:utf-8 -*-
import json
from django.contrib.auth.decorators import login_required
from utils.decorators import render_to
from models import Mail
import imaplib
from scripts import mailbox

@login_required
@render_to('mails.html')
def all(request, mail_id=0):
    title=''

    messages = []
    #mail = imaplib.IMAP4_SSL('imap.gmail.com')
    if mail_id == 0:
        title = 'All mails'
        login = Mail.objects.filter().all()[0].login
        password = Mail.objects.filter().all()[0].password
    else:
        title = Mail.objects.get(id=mail_id).login
        login = Mail.objects.get(id=mail_id).login
        password = Mail.objects.get(id=mail_id).password

    with mailbox.MailBox(login, password) as mbox:
        print mbox.get_count()
        messages = mbox.get_msgs(10)

    #mail.login(login, password)
    #mail.select("inbox")
    #typ, data = mail.search(None, 'ALL')
    #for num in data[0].split()[:10]:
    #    typ, data = mail.fetch(num, '(RFC822)')
    #    messages.append({ 'id': typ, 'data': data[0][1] })
    #mail.close()
    #mail.logout()
    return { 'active_page':'mails', 'active_mail':int(mail_id), 'mails':Mail.objects.filter(), 'title':title,
             'messages':messages }
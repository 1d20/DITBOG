from django.db import models

class Mail(models.Model):
    login = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    server = models.CharField(max_length=255)
    last_check = models.DateTimeField(verbose_name=u'Date', auto_now_add=True)
    def __unicode__(self):
        return u'%s %s' % (self.login, self.server)

class MarketEngine(models.Model):
    market = models.ForeignKey('theme.market', related_name='marketengine_market')
    engine = models.ForeignKey('theme.engine', related_name='marketengine_engine')
    mail = models.ForeignKey('mail.mail', related_name='marketengine_mail')
    market_login = models.CharField(max_length=255)
    market_pass = models.CharField(max_length=255)
    def __unicode__(self):
        return u'%s %s' % (self.market, self.engine)

class Message(models.Model):
    mail = models.ForeignKey('mail.mail', related_name='message_mail')
    sender = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    date = models.DateTimeField(verbose_name=u'Date', auto_now_add=True)
    new = models.BooleanField(default=True)
    def __unicode__(self):
        return u'%s %s' % (self.sender, self.date)
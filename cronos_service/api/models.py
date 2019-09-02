from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    device_id = models.CharField(max_length=20, unique=True)

    def __unicode__(self):
        return u'%s %s' % self.user, self.device_id


class Application(models.Model):
    SOCIAL = 1
    WORK = 2
    MESSAGE = 3
    OTHERS = 4
    APP_TYPE_CHOICES = [
        (SOCIAL, 'SOCIAL'),
        (WORK, 'WORK'),
        (MESSAGE, 'MESSAGE'),
        (OTHERS, 'OTHERS')
    ]
    application_name = models.CharField(unique=True, max_length=100)
    application_type = models.IntegerField(choices=APP_TYPE_CHOICES, default=OTHERS)

    def __unicode__(self):
        return u'%s' % self.application_name


class Notification(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.DateTimeField()
    count = models.IntegerField()

    def __unicode__(self):
        return u'%s %s' % self.profile.user.username, self.application.application_name
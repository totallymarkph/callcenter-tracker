from django.db import models
from django.conf import settings

class Team(models.Model):
    manager = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, default=None, on_delete=models.SET_NULL)
    team_name = models.CharField(max_length=100)

    def __str__(self):
        return self.team_name

class CallCenterAgent(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, null=True, default=None, on_delete=models.SET_NULL)

    def __str__(self):
        return self.user.name

class Call(models.Model):
    agent = models.ForeignKey(CallCenterAgent, on_delete=models.DO_NOTHING)
    ticket = models.CharField(max_length=16)
    SALE = 'SA'
    NONSALE = 'NS'
    SUBSCRIBER = 'SU'
    MISROUTED = 'MR'
    INVALID = 'IN'
    CALL_TYPE_CHOICES = (
        (SALE, 'Sale'),
        (NONSALE, 'No Sale'),
        (SUBSCRIBER, 'Subscriber'),
        (MISROUTED, 'Misrouted'),
        (INVALID, 'Invalid'),
    )
    call_types = models.CharField(
        max_length=2,
        choices=CALL_TYPE_CHOICES,
        default=SALE,
    )
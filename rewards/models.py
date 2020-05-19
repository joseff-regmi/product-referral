from django.db import models
from referrals.models import Refer


class Reward(models.Model):
    points = models.PositiveIntegerField()
    refer = models.ForeignKey(Refer, related_name='refer', on_delete=models.CASCADE)

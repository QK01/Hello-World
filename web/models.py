# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Expence(models.Model):

    text = models.CharField(max_length = 255)
    date = models.DateField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User)





from django.db import models

from core.models import TimeStampedModel


class User(TimeStampedModel):
    first_name   = models.CharField(max_length=20)
    last_name    = models.CharField(max_length=30)
    email        = models.EmailField(max_length=200)
    password     = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=50)

    class Meta:
        db_table = 'users'


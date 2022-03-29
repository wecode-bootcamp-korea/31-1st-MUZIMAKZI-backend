from django.db import models

class TimeStampedModel(models.Model):
    create_at  = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class User(TimeStampedModel):
    first_name   = models.CharField(max_length=20)
    last_name    = models.CharField(max_length=30)
    email        = models.CharField(max_length=200)
    password     = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=50)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.email


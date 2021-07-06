from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify

from django.contrib.auth.models import User
from django.conf import settings
User = settings.AUTH_USER_MODEL

class Address(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    street_address = models.CharField(max_length=250, default='')
    city = models.CharField(max_length=250, default='')
    state = models.CharField(max_length=250, default='')
    zip = models.CharField(max_length=250, default='')


    def __str__(self):
        return f'{self.user}'

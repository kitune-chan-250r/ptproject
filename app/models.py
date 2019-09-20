from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    TYPE_CHOICES = (('company','企業アカウント'),
                    ('general','一般アカウント'))

    acctype = models.CharField(choices=TYPE_CHOICES,max_length=100,default='general')
    acctext = models.TextField(blank=True,max_length=1000)

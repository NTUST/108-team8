from django.db import models
import datetime
from django.utils import timezone
# Create your models here.


#可能要棄用了
class Users(models.Model):
    name = models.CharField(max_length=100)
    email=models.CharField(max_length=150)
    password=models.CharField(max_length=100)
    user_account=models.CharField(max_length=100,primary_key=True)
    def __str__(self):
        return self.user_account
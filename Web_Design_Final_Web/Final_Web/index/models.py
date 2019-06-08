from django.db import models
import datetime
from django.utils import timezone
from login.models import Users
from django.contrib import auth

# Create your models here.
#Store資料表
class Store(models.Model):
    store_name = models.CharField(max_length=100)
    store_introduction=models.TextField(default='')
    store_image=models.ImageField(null=True,blank=True,width_field="store_image_width", height_field="store_image_height")
    store_image_width = models.IntegerField(default=0)
    store_image_height = models.IntegerField(default=0)
    store_address = models.TextField(default='')
    store_phone= models.CharField(max_length=13)
    store_opening_time = models.TextField(default='')
    introdution_createtime=models.DateTimeField('date published')
    account = models.ForeignKey(auth,on_delete=models.CASCADE)
    def __str__(self):
        return self.store_name


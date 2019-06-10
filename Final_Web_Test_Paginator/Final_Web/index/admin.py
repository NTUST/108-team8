from django.contrib import admin
from .models import Store
# Register your models here.

#讓admin存取Store資料表
admin.site.register(Store)


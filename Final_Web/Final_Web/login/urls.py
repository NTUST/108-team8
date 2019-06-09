from django.conf.urls import url
from . import views
#未完成，要跟著views.py一起
urlpatterns=[url(r'^$',views.login,name='login')]
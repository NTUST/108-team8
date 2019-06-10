from django.conf.urls import url
from . import views
app_name='index'
urlpatterns=[url(r'^$',views.index,name='index'),
    #單一店家的url
    url(r'^(?P<pk>[0-9]+)/$',views.StoreView.as_view(),name='store'),
    #-------------
    url(r'^shops/$',views.shops,name='shops')]
from django.conf.urls import url
from . import views
app_name='index'
urlpatterns=[url(r'^$',views.index,name='index'),
    #Store的url未完成
    url(r'^(?P<pk>[0-9]+)/$',views.StoreView.as_view(),name='store'),
    #url(r'^store/$',views.st,name='st'),
    url(r'^shops/$',views.shops,name='shops')]
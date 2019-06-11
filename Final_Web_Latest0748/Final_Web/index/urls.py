from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name='index'
urlpatterns=[
	url(r'^$',views.index,name='index'),
    #Store的url未完成
    #url(r'^store/(?P<pk>+)/$',views.store.as_view(),name='stores'),
    url(r'^shops/(?P<pk>[0-9]+)/$',views.StoreView.as_view(),name='store'),
    url(r'^shops/$',views.shops,name='shops'),
    url(r'^statement/$',views.statement,name='statement'),
    url(r'^fight/$',views.fight,name='fight'),
    url(r'^addStore/$',views.addStore,name='addstore'),
    # url(r'^createstore/$',views.crtStore,name='crtstore')
    ]

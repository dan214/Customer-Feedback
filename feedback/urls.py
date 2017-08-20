from django.conf.urls import url

from . import views
from .views import index

urlpatterns = [
    url(r'^$',index,name='list'),
    url(r'^thanks/$',views.thanks),
    url(r'^create/$',views.create_company),
    url(r'^(?P<company_id>[0-9]+)/$', views.detail, name='detail'),
]
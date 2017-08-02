from django.conf.urls import url

from . import views
from .views import index

urlpatterns = [
    url(r'^$',index.as_view()),
    url(r'^createuser/$',views.create_form, name='createuser'),
    url(r'^(?P<company_id>[0-9]+)/$', views.detail, name='detail'),
]
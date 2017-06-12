from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'^createuser/$',views.create_form, name='createuser'),
]
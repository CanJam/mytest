#！-*-coding：UTF-8-*-


from django.conf.urls import url
from django.urls import path
from . import views
app_name = 'banks'
urlpatterns = [
    url(r'^hello/$', views.hello,name= 'hello'),
]



from django.conf.urls import url
from . import views

url=[
    url(r'^$',views.index,name='index'),
]
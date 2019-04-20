from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views

app_name = 'voice'

urlpatterns = [
    url(r'^$', views.Index.as_view(), name='indexView'),
    # path('',views.index,name='indexView'),
    url(r'^submit/$',views.submit,name='submit'),
]

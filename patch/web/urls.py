from django.contrib import admin
from django.urls import path
from web.views import index


app_name = "web"

urlpatterns = [
    path('', index,name="home"),
]

from django.contrib import admin
from django.urls import path, include
from .views import index, contact


urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
]

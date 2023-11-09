from django.urls import path
from .views import index, contact, terms,    about




app_name = 'core'

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('terms/', terms, name='terms'),
    path('about/', about, name='about'),
]

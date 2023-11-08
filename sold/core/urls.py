from django.contrib import admin
from django.urls import path, include
from .views import index, contact, signup, terms,    about
from django.contrib.auth import views as auth_views
from .forms import LoginForm



app_name = 'core'

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('terms/', terms, name='terms'),
    path('about/', about, name='about'),
    path('signup/', signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(
        authentication_form=LoginForm,
        template_name='core/login.html'
    ), name='login'),

]

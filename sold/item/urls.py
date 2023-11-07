from django.urls import path, include

from .views import detail, new_item, delete, edit, items

app_name = 'item'

urlpatterns = [
    path('search', items, name='items'),
    path('items/<int:pk>/', detail, name='detail'),
    path('items/<int:pk>/delete/', delete, name='delete'),
    path('items/<int:pk>/edit/', edit, name='edit'),
    path('new/', new_item, name='new_item'),
]
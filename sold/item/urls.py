from django.urls import path, include

from .views import detail, new_item, delete, edit, items, category_list

app_name = 'item'

urlpatterns = [
    path('search', items, name='items'),
    path('items/<int:pk>/', detail, name='detail'),
    path('items/<int:pk>/delete/', delete, name='delete'),
    path('items/<int:pk>/edit/', edit, name='edit'),
    path('new/', new_item, name='new_item'),
    path('category/<slug:category_slug>/', category_list, name='category_list'),
]

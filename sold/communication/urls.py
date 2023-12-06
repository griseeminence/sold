from django.urls import path
from .views import new_communication, inbox, detail

app_name = 'communication'

urlpatterns = [
    path('inbox/', inbox, name='inbox'),
    path('inbox/<int:pk>/', detail, name='detail'),
    path('inbox/new/<int:item_pk>/', new_communication, name='new_communication'),
]

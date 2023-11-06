from django.urls import reverse_lazy, path
from .views import new_communication, inbox

app_name = 'communication'

urlpatterns = [
    path('inbox/', inbox, name='inbox'),
    path('inbox/new/<int:item_pk>/', new_communication, name='new_communication'),
]

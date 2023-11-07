from django.contrib import admin
from .models import CommunicationMessage, Communication

# Register your models here.


admin.site.register(CommunicationMessage)
admin.site.register(Communication)
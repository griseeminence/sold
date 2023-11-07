from django.contrib import admin
from .models import CommunicationMessage, Communication

admin.site.register(CommunicationMessage)
admin.site.register(Communication)

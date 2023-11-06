from django.contrib.auth import get_user_model
from django.db import models
from item.models import Item

# Create your models here.
User = get_user_model()


class Communication(models.Model):
    item = models.ForeignKey(Item, related_name='communications', on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name='communications', blank=True)

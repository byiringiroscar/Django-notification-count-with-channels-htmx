from django.db import models

# Create your models here.

class Notification(models.Model):
    count_not = models.PositiveIntegerField(default=0)
    name = models.CharField(max_length=100, default='Notification')


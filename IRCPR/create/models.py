from django.db import models
from django.contrib.auth.models import User


class CreateRoom(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="creator")
    create_list = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)


# Create your models here.

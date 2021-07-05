from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Room(models.Model):
    author = models.ForeignKey(User, related_name='user_rooms', on_delete=models.CASCADE)
    member = models.ManyToManyField(User, related_name='room_members')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ChatMessage(models.Model):
    sender = models.ForeignKey(User, related_name='user_sender', on_delete=models.CASCADE)
    room = models.ForeignKey(Room,related_name="room_messages",on_delete=models.CASCADE)
    message = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created_at',)

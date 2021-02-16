import string
import random
from django.db import models

# Create your models here.

def generate_room_id():
    length = 8
    while True:
        room_id = ''.join(random.choices(string.ascii_uppercase, k=length))
        if Room.objects.filter(code=room_id).count() == 0:
            break
    return room_id


class Room(models.Model):
    code = models.CharField(max_length=8, default="", unique=True)
    host = models.CharField(max_length=50, unique=True)
    guest_can_pause = models.BooleanField(null=False, default=False)
    votes_to_skip = models.IntegerField(null=False, default=1)
    created_at = models.DateTimeField(auto_now_add=True)

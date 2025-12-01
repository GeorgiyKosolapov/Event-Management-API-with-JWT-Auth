from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class Event(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    date = models.DateTimeField()
    location = models.CharField(max_length=100)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="events")
    participants = models.ManyToManyField(User, related_name="attended_events", blank=True)

    def __str__(self):
        return self.title

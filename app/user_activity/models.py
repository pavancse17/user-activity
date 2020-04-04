import pytz
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))
    id = models.CharField(primary_key=True, max_length=255)
    email = models.EmailField( unique=True)
    username = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    timezone = models.CharField(max_length=32, choices=TIMEZONES, default='UTC')
    real_name = models.CharField(max_length=255)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class ActivityPeriod(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    user = models.ForeignKey("user_activity.User", on_delete=models.CASCADE, related_name="activities")

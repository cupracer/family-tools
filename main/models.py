from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    todoist_api_key = models.CharField(null=True, blank=False, max_length=40)

    def __str__(self):
        if self.get_full_name():
            return self.get_full_name()
        else:
            return self.get_username()

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    def __str__(self):
        if self.get_full_name():
            return self.get_full_name()
        else:
            return self.get_username()

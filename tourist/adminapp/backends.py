# adminapp/backends.py
from django.contrib.auth.backends import ModelBackend
from .models import User

class CustomUserBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(username=username,password=password)
        except User.DoesNotExist:
            return None

        return None
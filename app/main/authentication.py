from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User

from .models import News, User

class UserBackend(ModelBackend):
    '''Custom authentication backend'''
    def authenticate(self, request, token=None):
        try:
            user = User.objects.get(token=token)
            if user is not None:
                return user
        except User.DoesNotExist:
            pass

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

    
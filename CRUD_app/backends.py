from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from django.db.models import Q



class EmailOrUsernameBackend(ModelBackend):
    '''This class overrides the authenticate method to allow users to log in with either their username or email address.'''
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username) | Q(email=username))
        except User.DoesNotExist:
            return None
        if user.check_password(password):
            return user
        return None


# Custom authentication backend VIP <------- also added in settings.pys
# AUTHENTICATION_BACKENDS = [
#     'CRUD_app.backends.EmailOrUsernameBackend',  # use your app name
#     'django.contrib.auth.backends.ModelBackend', # keep this for admin login
# ]
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import exceptions
from django.utils.functional import SimpleLazyObject
from django.contrib.auth.models import AnonymousUser

class CustomJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        header = self.get_header(request)
        if header is None:
            return None

        raw_token = self.get_raw_token(header)
        if raw_token is None:
            return None

        validated_token = self.get_validated_token(raw_token)
        return self.get_user(validated_token), validated_token

def get_user(request):
    user = None
    try:
        user_auth_tuple = CustomJWTAuthentication().authenticate(request)
        if user_auth_tuple is not None:
            user, token = user_auth_tuple
    except exceptions.AuthenticationFailed:
        user = AnonymousUser()
    return user or AnonymousUser()

class JWTAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        request.user = SimpleLazyObject(lambda: get_user(request))
        return self.get_response(request)

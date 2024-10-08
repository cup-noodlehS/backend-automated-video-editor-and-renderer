from rest_framework_simplejwt.authentication import JWTAuthentication
from django.utils.functional import SimpleLazyObject
from django.contrib.auth.models import AnonymousUser

def get_user(request):
    user = None
    try:
        user_auth_tuple = JWTAuthentication().authenticate(request)
        if user_auth_tuple is not None:
            user, token = user_auth_tuple
    except Exception:
        user = AnonymousUser()
    return user or AnonymousUser()

class JWTAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.user = SimpleLazyObject(lambda: get_user(request))
        return self.get_response(request)

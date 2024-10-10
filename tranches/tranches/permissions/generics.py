from rest_framework.permissions import BasePermission


class AdminCreatetOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return request.user.is_authenticated and request.user.is_admin
        return request.user.is_authenticated


class AdminViewOnly(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_admin


class AdminDeleteOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'DELETE':
            return request.user.is_authenticated and request.user.is_admin
        return request.user.is_authenticated


class AdminUpdateOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'PUT':
            return request.user.is_authenticated and request.user.is_admin
        return request.user.is_authenticated


class LoginRequired(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated

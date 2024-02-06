from rest_framework import permissions
from users.models import User
from rest_framework.views import Request
import ipdb


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request: Request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
            and request.user.is_superuser
        )


class IsEmployeeAndAuthenticated(permissions.BasePermission):
    def has_permission(self, request: Request, view):
        return request.user.is_authenticated and request.user.is_superuser


class IsMovieOwnerAndNotEmployee(permissions.BasePermission):
    def has_object_permission(self, request: Request, view, obj: User):
        return request.user == obj

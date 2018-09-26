from rest_framework import permissions
from django.shortcuts import get_object_or_404


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.IsAmin == request.user


class IsActiveAndAdmin(permissions.IsAdminUser):
    def has_permission(self, request, view):
        is_admin = super(IsActiveAndAdmin, self).has_permission(request, view)
        return request.user.is_active and is_admin

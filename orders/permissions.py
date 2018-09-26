from rest_framework import permissions


class IsActiveAndUser(permissions.IsAuthenticatedOrReadOnly):
    def has_permission(self, request, view):
        is_user = super(IsActiveAndUser, self).has_permission(request, view)
        return request.user.is_active and is_user

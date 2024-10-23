from rest_framework import permissions

class IsAuthenticatedOrAdmin(permissions.BasePermission):
    """
    Custom permission to only allow authenticated or admin users.
    """

    def has_permission(self, request, view):
        # Check if the user is authenticated or an admin
        return request.user and (request.user.status in ['authenticated', 'admin'])

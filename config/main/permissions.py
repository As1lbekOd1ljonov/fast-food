from rest_framework.permissions import BasePermission, SAFE_METHODS

class Permission(BasePermission):


    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        if request.method == 'POST':
            return request.user and request.user.is_staff
        return True

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return request.user.is_staff

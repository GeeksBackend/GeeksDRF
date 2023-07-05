from rest_framework.permissions import BasePermission

class ChatPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(obj.from_user.pk == request.user.pk or obj.to_user.pk == request.user.pk)
from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthorOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        user = request.user
        if view.action =='create':
            return True
        article = view.get_object()
        if article.author.id == user.id:
            return ...



class IsUserReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        user = request.user
        if view.action == 'create':
            return True
        username = view.get_object()
        return request.user.id == user.id


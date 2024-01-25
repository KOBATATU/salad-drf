from rest_framework.permissions import BasePermission
class IsOwner(BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """
    #以下のようにエラーメッセージを定義できる
    message = 'Adding customers not allowed.'

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.

        # Instance must have an attribute named `owner`.
        print(obj)
        return obj == request.user
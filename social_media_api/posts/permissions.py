from rest_framework.permissions import BasePermission
# the base permission allows creation of custom permissions
class IsAuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ['GET', 'HEAD', 'OPTIONS']: #checks if the methods is one of the safe method that is used to retrieve data
            return True # if the request is a safe one like get or head the method returns true meaning the user is granted to view
        return obj.author == request.user # checks if the person making the request is the author of the object
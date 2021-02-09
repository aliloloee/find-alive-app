from customUser.models import MyUser
from rest_framework import permissions


## Just superuser
class IsStaff(permissions.BasePermission) :
    def has_permission(self, request, view) :
        try :
            user = MyUser.objects.get(user_name=request.query_params['username'])
        except :
            return False

        if request.user.is_staff :
            return True

        # if not user == request.user :
        #     return False
        # else :
        #     return True



## Just superuser
class IsSuper(permissions.BasePermission) :
    def has_permission(self, request, view) :
        try :
            user = MyUser.objects.get(user_name=request.query_params['username'])
        except :
            return False

        if request.user.is_superuser :
            return True

        # if not user == request.user :
        #     return False
        # else :
        #     return True

class IsOwner(permissions.BasePermission) :
    def has_permission(self, request, view) :
        try :
            user = MyUser.objects.get(user_name=request.query_params['username'])
        except :
            return False

        # if request.user.is_superuser :
        #     return True

        if not user == request.user :
            return False
        else :
            return True
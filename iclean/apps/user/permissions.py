from rest_framework import permissions


class IsStaffOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.is_staff or request.method in permissions.SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or request.method in permissions.SAFE_METHODS


class IsStaff(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.is_staff

    def has_object_permission(self, request, view, obj):
        return request.user.is_staff


class IsClientUser(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return obj.email == request.user.email


class IsCompanyUser(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return obj.email == request.user.email


class IsClient(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role.role == 'client'

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user and obj.user.role.role == 'client'


class IsCompany(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role.role == 'company'

    def has_object_permission(self, request, view, obj):
        return obj.user.id == request.user.id and obj.user.role.role == 'company'
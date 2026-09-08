from rest_framework import permissions

class IsEditorOrReadOnly(permissions.BasePermission):
    """Allow safe methods to everyone, editorial write operations only to Editors/Admins."""
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return (
            request.user and
            request.user.is_authenticated and
            request.user.role in ['EDITOR', 'SENIOR_EDITOR', 'ADMIN']
        )

class IsAuthorOrEditor(permissions.BasePermission):
    """Allow authors to modify their own drafts, editors to modify anything."""
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if not (request.user and request.user.is_authenticated):
            return False
        if request.user.role in ['EDITOR', 'SENIOR_EDITOR', 'ADMIN']:
            return True
        # Check if user is author
        if hasattr(obj, 'authors') and hasattr(request.user, 'author_profile'):
            return obj.authors.filter(id=request.user.author_profile.id).exists()
        return False

from rest_framework import viewsets, permissions
from .models import AuthorProfile
from .serializers import AuthorProfileSerializer

class AuthorProfileViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AuthorProfile.objects.all()
    serializer_class = AuthorProfileSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'slug'
    pagination_class = None

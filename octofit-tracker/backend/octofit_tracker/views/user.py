from rest_framework import viewsets
from octofit_tracker.models.user import UserProfile
from octofit_tracker.serializers.user import UserProfileSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

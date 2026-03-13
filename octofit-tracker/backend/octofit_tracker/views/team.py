from rest_framework import viewsets
from octofit_tracker.models.team import Team
from octofit_tracker.serializers.team import TeamSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

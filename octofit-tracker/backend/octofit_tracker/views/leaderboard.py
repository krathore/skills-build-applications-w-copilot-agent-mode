from rest_framework import viewsets
from octofit_tracker.models.leaderboard import LeaderboardEntry
from octofit_tracker.serializers.leaderboard import LeaderboardEntrySerializer

class LeaderboardEntryViewSet(viewsets.ModelViewSet):
    queryset = LeaderboardEntry.objects.all()
    serializer_class = LeaderboardEntrySerializer

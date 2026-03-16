from rest_framework import serializers
from octofit_tracker.models.leaderboard import LeaderboardEntry

class LeaderboardEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaderboardEntry
        fields = '__all__'

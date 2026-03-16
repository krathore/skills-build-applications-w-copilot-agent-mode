from django.contrib import admin
from octofit_tracker.models.user import UserProfile
from octofit_tracker.models.activity import ActivityLog
from octofit_tracker.models.team import Team
from octofit_tracker.models.leaderboard import LeaderboardEntry
from octofit_tracker.models.workout import WorkoutSuggestion

admin.site.register(UserProfile)
admin.site.register(ActivityLog)
admin.site.register(Team)
admin.site.register(LeaderboardEntry)
admin.site.register(WorkoutSuggestion)

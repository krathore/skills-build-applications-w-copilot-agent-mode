from rest_framework import viewsets
from octofit_tracker.models.activity import ActivityLog
from octofit_tracker.serializers.activity import ActivityLogSerializer

class ActivityLogViewSet(viewsets.ModelViewSet):
    queryset = ActivityLog.objects.all()
    serializer_class = ActivityLogSerializer

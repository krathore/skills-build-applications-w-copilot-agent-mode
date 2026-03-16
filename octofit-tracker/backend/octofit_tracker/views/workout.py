from rest_framework import viewsets
from octofit_tracker.models.workout import WorkoutSuggestion
from octofit_tracker.serializers.workout import WorkoutSuggestionSerializer

class WorkoutSuggestionViewSet(viewsets.ModelViewSet):
    queryset = WorkoutSuggestion.objects.all()
    serializer_class = WorkoutSuggestionSerializer

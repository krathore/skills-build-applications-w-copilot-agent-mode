from rest_framework import serializers
from octofit_tracker.models.workout import WorkoutSuggestion

class WorkoutSuggestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutSuggestion
        fields = '__all__'

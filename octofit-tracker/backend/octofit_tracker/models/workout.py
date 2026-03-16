from djongo import models
from .user import UserProfile

class WorkoutSuggestion(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    suggestion = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.suggestion[:30]}..."

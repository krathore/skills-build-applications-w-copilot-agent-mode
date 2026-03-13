"""
URL configuration for octofit_tracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from octofit_tracker.views.user import UserProfileViewSet
from octofit_tracker.views.activity import ActivityLogViewSet
from octofit_tracker.views.team import TeamViewSet
from octofit_tracker.views.leaderboard import LeaderboardEntryViewSet
from octofit_tracker.views.workout import WorkoutSuggestionViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse as drf_reverse

router = routers.DefaultRouter()
router.register(r'users', UserProfileViewSet)
router.register(r'activities', ActivityLogViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'leaderboard', LeaderboardEntryViewSet)
router.register(r'workouts', WorkoutSuggestionViewSet)

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': drf_reverse('userprofile-list', request=request, format=format),
        'activities': drf_reverse('activitylog-list', request=request, format=format),
        'teams': drf_reverse('team-list', request=request, format=format),
        'leaderboard': drf_reverse('leaderboardentry-list', request=request, format=format),
        'workouts': drf_reverse('workoutsuggestion-list', request=request, format=format),
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', api_root, name='api-root'),
]

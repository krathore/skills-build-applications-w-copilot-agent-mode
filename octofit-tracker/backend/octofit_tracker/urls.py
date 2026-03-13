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


import os

@api_view(['GET'])
def api_root(request, format=None):
    codespace_name = os.environ.get('CODESPACE_NAME')
    if codespace_name:
        base_url = f"https://{codespace_name}-8000.app.github.dev/api"
    else:
        base_url = f"http://{request.get_host()}/api"
    return Response({
        'users': f'{base_url}/users/',
        'activities': f'{base_url}/activities/',
        'teams': f'{base_url}/teams/',
        'leaderboard': f'{base_url}/leaderboard/',
        'workouts': f'{base_url}/workouts/',
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', api_root, name='api-root'),
]

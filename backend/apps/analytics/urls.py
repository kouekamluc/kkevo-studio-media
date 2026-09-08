from django.urls import path
from .views import NewsroomStatsView

urlpatterns = [
    path('newsroom-stats/', NewsroomStatsView.as_view(), name='newsroom-stats'),
]

"""
URL mappings for the feed APIs.
"""
from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter

from feed import views


router = DefaultRouter()
router.register("feed", views.PostListViewSet)
router.register("post", views.PostDetailViewSet)

app_name = "feed"

urlpatterns = [
    path("", include(router.urls)),
]

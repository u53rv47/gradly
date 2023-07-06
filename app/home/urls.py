"""
URL mappings for the home APIs.
"""
from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter

from home import views


router = DefaultRouter()
router.register("domains", views.DomainViewSet)
router.register("communities", views.CommunityViewSet)
router.register("feed", views.CommunityViewSet)


app_name = "home"

urlpatterns = [
    path("", include(router.urls)),
]

from django.urls import path
from .views import ChatAPIView, APIKeyValidationView

urlpatterns = [
    path("", ChatAPIView.as_view(), name="chat-api"),
    path("auth/", APIKeyValidationView.as_view(), name="authentication-api"),
]

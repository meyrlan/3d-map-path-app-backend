from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from api.v2.client.views import (
    ProfileAPIView,
    EventsAPIView,
    ListEventsAPIView,
    DataSetAPIView,
    ListDataSetsAPIView
)

router = routers.SimpleRouter(trailing_slash=False)

urlpatterns = [
    # path("profile/<int:pk>", ProfileAPIView.as_view(), name="profile"),
    # path("event/<int:pk>", EventsAPIView.as_view(), name="event"),
    # path("events", ListEventsAPIView.as_view(), name="events"),
    path('dataset/<int:pk>', DataSetAPIView.as_view(), name='get_dataset'),
    path("datasets", ListDataSetsAPIView.as_view(), name="datasets"),
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh')
] + router.urls

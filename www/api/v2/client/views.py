from rest_framework.generics import RetrieveUpdateAPIView, RetrieveAPIView, ListAPIView
from rest_framework.permissions import AllowAny
from api.v2.client.serializers import ProfileSerializer, EventSerializer, ShortDataSetSerializer, DataSetSerializer
from core.models import Profile, Event, DataSet


# --- Views ---


class ProfileAPIView(RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [AllowAny]


class EventsAPIView(RetrieveAPIView):
    http_method_names = ["get"]
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [AllowAny]


class ListEventsAPIView(ListAPIView):
    http_method_names = ["get"]
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [AllowAny]


class ListDataSetsAPIView(ListAPIView):
    http_method_names = ["get"]
    queryset = DataSet.objects.all()
    serializer_class = ShortDataSetSerializer
    permission_classes = [AllowAny]


class DataSetAPIView(RetrieveAPIView):
    http_method_names = ["get"]
    queryset = DataSet.objects.all()
    serializer_class = DataSetSerializer
    permission_classes = [AllowAny]

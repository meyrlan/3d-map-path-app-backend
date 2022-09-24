from rest_framework.generics import CreateAPIView
from location.models import Location
from location.serializers import LocationSerializer


class LocationCreateAPIView(CreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

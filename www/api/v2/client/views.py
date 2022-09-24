from rest_framework.generics import RetrieveUpdateAPIView, RetrieveAPIView, ListAPIView, CreateAPIView
from rest_framework.permissions import AllowAny
from api.v2.client.serializers import ProfileSerializer, EventSerializer, ShortDataSetSerializer, DataSetSerializer, ExcelDataSerializer, DataInstanceSerializer
from core.models import Profile, Event, DataSet
from external_api import interpolate_road_points
from rest_framework.response import Response


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


class InterpolatedDataSetAPIView(RetrieveAPIView):
    http_method_names = ["get"]
    queryset = DataSet.objects.all()
    serializer_class = DataSetSerializer
    permission_classes = [AllowAny]

    def retrieve(self, request, *args, **kwargs):
        queryset = self.queryset.get(pk=kwargs['pk'])
        data = {'identifier': queryset.identifier, 'data_instances': []}
        interpolate = []
        for instance in queryset.data_instances.all():
            if instance.activity == 'driving':
                interpolate.append(f'{instance.lat},{instance.lng}')
            elif len(interpolate) != 0:
                interpolated_points = interpolate_road_points('|'.join(interpolate))
                for point in interpolated_points:
                    data['data_instances'].append({
                        'lat': point['latitude'],
                        'lng': point['longitude'],
                        'alt': 0,
                        'identifier': None,
                        'timestamp': 0,
                        'floor': None,
                        'horizontal_accuracy': 0,
                        'vertical_accuracy': 0,
                        'confidence': 0.0,
                        'activity': 'driving',
                    })
                interpolate = []
            data['data_instances'].append(DataInstanceSerializer(instance).data)
        if len(interpolate) != 0:
            interpolated_points = interpolate_road_points('|'.join(interpolate))
            for point in interpolated_points:
                data['data_instances'].append({
                    'lat': point['latitude'],
                    'lng': point['longitude'],
                    'alt': 0,
                    'identifier': None,
                    'timestamp': 0,
                    'floor': None,
                    'horizontal_accuracy': 0,
                    'vertical_accuracy': 0,
                    'confidence': 0.0,
                    'activity': 'driving',
                })
        return Response(data)

from rest_framework.generics import RetrieveUpdateAPIView, RetrieveAPIView, ListAPIView, CreateAPIView
from rest_framework.permissions import AllowAny
from api.v2.client.serializers import ProfileSerializer, EventSerializer, ShortDataSetSerializer, DataSetSerializer, ExcelDataSerializer, DataInstanceSerializer
from core.models import Profile, Event, DataSet
from external_api import interpolate_road_points
from rest_framework.response import Response
from scipy import interpolate


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
        if queryset.data_instances.count() == 1:
            data['data_instances'].append(DataInstanceSerializer(queryset.data_instances.first()).data)
            return Response(data)
        interpolate1 = []
        x, y, z, t = [], [], [], []
        for instance in queryset.data_instances.all():
            x.append(instance.lat)
            y.append(instance.lng)
            z.append(instance.alt)
            t.append(instance.timestamp)
        #     if instance.activity == 'driving':
        #         interpolate.append(f'{instance.lat},{instance.lng}')
        #     elif len(interpolate) != 0:
        #         interpolated_points = interpolate_road_points('|'.join(interpolate))
        #         for point in interpolated_points:
        #             data['data_instances'].append({
        #                 'lat': point['latitude'],
        #                 'lng': point['longitude'],
        #                 'alt': 0,
        #                 'identifier': None,
        #                 'timestamp': 0,
        #                 'floor': None,
        #                 'horizontal_accuracy': 0,
        #                 'vertical_accuracy': 0,
        #                 'confidence': 0.0,
        #                 'activity': 'driving',
        #             })
        #         interpolate = []
        #     if instance.activity != 'driving':
        #         data['data_instances'].append(DataInstanceSerializer(instance).data)
        # if len(interpolate) != 0:
        #     interpolated_points = interpolate_road_points('|'.join(interpolate))
        #     for point in interpolated_points:
        #         data['data_instances'].append({
        #             'lat': point['latitude'],
        #             'lng': point['longitude'],
        #             'alt': 0,
        #             'identifier': None,
        #             'timestamp': 0,
        #             'floor': None,
        #             'horizontal_accuracy': 0,
        #             'vertical_accuracy': 0,
        #             'confidence': 0.0,
        #             'activity': 'driving',
        #         })
        sx = interpolate.InterpolatedUnivariateSpline(t, x)
        sy = interpolate.InterpolatedUnivariateSpline(t, y)
        sz = interpolate.InterpolatedUnivariateSpline(t, z)
        start_time = t[0]
        end_time = t[-1]
        dt = (t[-1] - t[0]) // 100
        while start_time < end_time:
            data['data_instances'].append({
                'lat': sx(start_time),
                'lng': sy(start_time),
                'alt': sz(start_time),
                'identifier': None,
                'timestamp': start_time,
                'floor': None,
                'horizontal_accuracy': 0,
                'vertical_accuracy': 0,
                'confidence': 0.0,
                'activity': 'driving',
            })
            start_time += dt
        return Response(data)

from rest_framework import serializers
from location.models import Location


class LocationSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        many = kwargs.pop('many', True)
        super(LocationSerializer, self).__init__(many=many, *args, **kwargs)

    class Meta:
        model = Location
        fields = "__all__"

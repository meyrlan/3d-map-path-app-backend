import logging

from rest_framework import serializers
from drf_spectacular.utils import extend_schema_field

from core.models import (
    Profile,
    Event,
    DataSet,
    DataInstance,
)

logger = logging.getLogger(__name__)


class ProfileSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source="user_id", read_only=True)
    sex = serializers.CharField(source="get_sex_display")
    interests = serializers.StringRelatedField(many=True)
    user = serializers.StringRelatedField()

    class Meta:
        model = Profile
        fields = [
            "id",
            "first_name",
            "last_name",
            "sex",
            "birth_date",
            "bio",
            "interests",
            "user"
        ]


class EventSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    attendees = serializers.SerializerMethodField()
    capacity = serializers.IntegerField()
    date_time = serializers.DateTimeField()
    age_limit = serializers.IntegerField(allow_null=True)
    description = serializers.CharField()
    owner = ProfileSerializer()
    interests = serializers.SerializerMethodField()

    @extend_schema_field(ProfileSerializer(many=True))
    def get_attendees(self, event):
        return ProfileSerializer(event.attendees.all(), many=True, context=self.context).data

    def get_interests(self, event):
        return [interest.title for interest in event.interests.all()]

    class Meta:
        model = Event
        fields = [
            "id",
            "title",
            "capacity",
            "date_time",
            "age_limit",
            "description",
            "owner",
            "interests",
            "attendees",
        ]


class DataInstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataInstance
        fields = [
            "lat",
            "lng",
            "alt",
            "identifier",
            "timestamp",
            "floor",
            "horizontal_accuracy",
            "vertical_accuracy",
            "confidence",
            "activity",
        ]


class DataSetSerializer(serializers.ModelSerializer):
    data_set = DataInstanceSerializer()

    class Meta:
        model = DataSet
        fields = [
            "identifier",
        ]


class ShortDataSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataSet
        fields = [
            "identifier",
        ]

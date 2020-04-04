from rest_framework import serializers

from user_activity.models import User, ActivityPeriod


class ActivitySerializer(serializers.ModelSerializer):
    start_time = serializers.DateTimeField(format="%b %d %Y %I:%M:%S%p")
    end_time = serializers.DateTimeField(format="%b %d %Y %I:%M:%S%p")

    class Meta:
        model = ActivityPeriod
        fields = ["start_time", "end_time"]

class UserActivitySerializer(serializers.ModelSerializer):
    tz = serializers.CharField(source="timezone")
    activity_periods = ActivitySerializer(source="activities", many=True)

    class Meta:
        model = User
        fields = ["id", "real_name", "tz", "activity_periods"]

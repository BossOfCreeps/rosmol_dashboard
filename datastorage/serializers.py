from rest_framework import serializers

from datastorage.models import DataValue


class DataValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataValue
        fields = "__all__"

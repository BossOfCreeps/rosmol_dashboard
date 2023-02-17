from rest_framework import serializers

from datastorage.models import DataValue, DataSection, DataCriteria, DataName, Area


class DataSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataSection
        fields = "__all__"


class DataCriteriaSerializer(serializers.ModelSerializer):
    unit = serializers.CharField(source="unit.name")

    class Meta:
        model = DataCriteria
        fields = "__all__"


class DataNameSerializer(serializers.ModelSerializer):
    sub_names = serializers.SerializerMethodField()

    @staticmethod
    def get_sub_names(obj):
        return DataNameSerializer(obj.sub_names.all(), many=True).data

    class Meta:
        model = DataName
        fields = ("id", "name", "section", "sub_names")


class AreaSerializer(serializers.ModelSerializer):
    sub_areas = serializers.SerializerMethodField()

    @staticmethod
    def get_sub_areas(obj):
        return AreaSerializer(obj.sub_areas.all(), many=True).data

    class Meta:
        model = Area
        fields = ("id", "name", "sub_areas")


class DataValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataValue
        fields = "__all__"

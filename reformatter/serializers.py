from collections import OrderedDict

from rest_framework import serializers

from datastorage.models import DataValue, Area


class DateSerializer(serializers.Serializer):  # noqa
    month = serializers.IntegerField(required=False, allow_null=True)
    year = serializers.IntegerField()


class ReformatterRequest(serializers.Serializer):  # noqa
    name_filter = serializers.ListField(child=serializers.IntegerField(), required=False)
    crit_filter = serializers.ListField(child=serializers.IntegerField(), required=False)
    area_filter = serializers.ListField(child=serializers.UUIDField(), required=False)
    date_filter = serializers.ListField(child=DateSerializer(), required=False)

    name_equal = serializers.ListField(child=serializers.IntegerField(), required=False)
    crit_equal = serializers.ListField(child=serializers.IntegerField(), required=False)
    area_equal = serializers.ListField(child=serializers.UUIDField(), required=False)
    date_equal = serializers.ListField(child=DateSerializer(), required=False)

    filter_param = None

    def validate(self, attrs: OrderedDict):
        filter_key = None
        for key, value in attrs.items():
            if key.endswith("_filter") and value is not None:
                if filter_key is not None:
                    raise serializers.ValidationError("Several filters")
                filter_key = key.split("_")[0]
                self.filter_param = key

        equal_counter = 0
        for key, value in attrs.items():
            if key.endswith("_equal") and value is not None:
                equal_counter += 1
                if key.startswith(filter_key):
                    raise serializers.ValidationError("One field to filter and equal")
        if equal_counter != 3:
            raise serializers.ValidationError("You need call more equals params")

        return attrs

    def get_filtered_values_by_equals(self):
        query = DataValue.objects.all()

        if self.validated_data.get("name_equal") is not None:
            query = query.filter(name_id__in=self.validated_data.get("name_equal"))

        if self.validated_data.get("crit_equal") is not None:
            query = query.filter(criteria_id__in=self.validated_data.get("crit_equal"))

        if self.validated_data.get("area_equal") is not None:
            query = query.filter(area_id__in=self.validated_data.get("area_equal"))

        if self.validated_data.get("date_equal") is not None:
            ids = []
            for date_equal in self.validated_data.get("date_equal"):
                _query = query.filter(date__year=date_equal.get("year"))
                if date_equal.get("month") is not None:
                    _query = _query.filter(date__month=date_equal.get("month"))
                ids.extend([q.id for q in _query])
            query = query.filter(id__in=ids)

        return query


class CreateCSVRequest(serializers.Serializer):  # noqa
    headers = serializers.ListField(child=serializers.CharField())
    names = serializers.ListField(child=serializers.CharField())
    data = serializers.ListField(child=serializers.ListField(child=serializers.CharField()))

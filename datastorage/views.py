from rest_framework import viewsets

from datastorage.models import DataValue
from datastorage.serializers import DataValueSerializer


class DataViewSet(viewsets.ModelViewSet):
    serializer_class = DataValueSerializer
    queryset = DataValue.objects.all()

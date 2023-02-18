from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics

from datastorage.models import DataValue, DataSection, DataCriteria, DataName, Area
from datastorage.serializers import DataValueSerializer, DataSectionSerializer, DataCriteriaSerializer, \
    DataNameSerializer, AreaSerializer


class DataSectionAPIView(generics.ListAPIView):
    serializer_class = DataSectionSerializer
    queryset = DataSection.objects.all()


class DataCriteriaAPIView(generics.ListAPIView):
    serializer_class = DataCriteriaSerializer
    queryset = DataCriteria.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['section']


class DataNameAPIView(generics.ListAPIView):
    serializer_class = DataNameSerializer
    queryset = DataName.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['section']


class AreaAPIView(generics.ListAPIView):
    serializer_class = AreaSerializer
    queryset = Area.objects.all()


class DataViewSet(viewsets.ModelViewSet):
    serializer_class = DataValueSerializer
    queryset = DataValue.objects.all()

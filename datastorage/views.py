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


class DataNameAPIView(generics.ListAPIView):
    serializer_class = DataNameSerializer
    queryset = DataName.objects.filter(head=None)


class AreaAPIView(generics.ListAPIView):
    serializer_class = AreaSerializer
    queryset = Area.objects.filter(head=None)


class DataViewSet(viewsets.ModelViewSet):
    serializer_class = DataValueSerializer
    queryset = DataValue.objects.all()

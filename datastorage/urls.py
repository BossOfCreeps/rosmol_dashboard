from django.urls import path
from rest_framework.routers import DefaultRouter

from datastorage.views import DataViewSet, DataSectionAPIView, DataCriteriaAPIView, DataNameAPIView, AreaAPIView

urlpatterns = [
    path('sections/', DataSectionAPIView.as_view(), name='sections'),
    path('criteria/', DataCriteriaAPIView.as_view(), name='criteria'),
    path('names/', DataNameAPIView.as_view(), name='names'),
    path('areas/', AreaAPIView.as_view(), name='areas'),
]

router = DefaultRouter()
router.register(r'', DataViewSet, basename='datastorage')
urlpatterns += router.urls

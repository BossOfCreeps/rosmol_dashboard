from rest_framework.routers import DefaultRouter

from datastorage.views import DataViewSet

router = DefaultRouter()
router.register(r'', DataViewSet, basename='datastorage')
urlpatterns = router.urls

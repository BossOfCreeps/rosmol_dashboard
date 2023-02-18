from django.urls import path

from reformatter.views import ReformatterAPIView, CreateCSVAPIView

urlpatterns = [
    path('', ReformatterAPIView.as_view(), name='reformatter'),
    path('svg/', CreateCSVAPIView.as_view(), name='create_svg'),
]

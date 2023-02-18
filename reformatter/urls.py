from django.urls import path

from reformatter.views import ReformatterAPIView

urlpatterns = [
    path('reformatter/', ReformatterAPIView.as_view(), name='reformatter'),
]

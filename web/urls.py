from django.urls import path

from web.views import Test

urlpatterns = [
    path('', Test.as_view(), name='web'),
]

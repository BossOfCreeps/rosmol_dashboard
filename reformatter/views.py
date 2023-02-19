import csv
from io import StringIO

from django.http import HttpResponse
from drf_yasg.utils import swagger_auto_schema
from rest_framework import views, status
from rest_framework.response import Response

from reformatter.serializers import ReformatterRequest, CreateCSVRequest


class ReformatterAPIView(views.APIView):
    @swagger_auto_schema(request_body=ReformatterRequest)
    def post(self, request):
        data = ReformatterRequest(data=request.data)
        if not data.is_valid():
            return Response(data.errors, status.HTTP_422_UNPROCESSABLE_ENTITY)

        values = data.get_filtered_values_by_equals()
        filter_param_name = data.filter_param
        results = []
        for param in data.validated_data.get(filter_param_name):
            result = None

            if filter_param_name == "name_filter":
                result = sum(value.value for value in values.filter(name_id=param))

            elif filter_param_name == "crit_filter":
                result = sum(value.value for value in values.filter(criteria_id=param))

            elif filter_param_name == "area_filter":
                result = sum(value.value for value in values.filter(area_id__in=param))

            elif filter_param_name == "date_filter":
                temp = values.filter(date__year=param.get("year"))
                if param.get("month"):
                    temp = temp.filter(date__month=param.get("month"))
                result = sum(value.value for value in temp)

            results.append(result)

        return Response(results)


class CreateCSVAPIView(views.APIView):
    @swagger_auto_schema(request_body=CreateCSVRequest)
    def post(self, request):
        data = CreateCSVRequest(data=request.data)
        if not data.is_valid():
            return Response(data.errors, status.HTTP_422_UNPROCESSABLE_ENTITY)

        file = StringIO()
        writer = csv.writer(file)
        writer.writerow([""] + data.validated_data["headers"])
        for i, row in enumerate(data.validated_data["data"]):
            writer.writerow([data.validated_data["names"][i]] + row)

        response = HttpResponse(file.getvalue(), content_type='application/csv')
        response['Content-Disposition'] = 'attachment; filename="file.csv"'
        return response

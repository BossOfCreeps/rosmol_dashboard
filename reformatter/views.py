from typing import Optional, List

from drf_yasg.utils import swagger_auto_schema
from rest_framework import views, status
from rest_framework.response import Response

from reformatter.serializers import ReformatterRequest


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
            if filter_param_name == "name_filter":
                results.append(values.filter(name_id=param).first())
            elif filter_param_name == "crit_filter":
                results.append(values.filter(criteria_id=param).first())
            elif filter_param_name == "area_equal":
                results.append(values.filter(area_id=param).first())
            elif filter_param_name == "date_equal":
                temp = values.filter(date__year=param.get("year"))
                if param.get("month"):
                    temp = temp.filter(date__month=param.get("month"))
                results.append(temp.first())

        return Response([
            result.value if result else None
            for result in results
        ])

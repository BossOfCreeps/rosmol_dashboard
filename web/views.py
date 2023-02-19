from django.shortcuts import render
from django.views import View

from datastorage.models import Area, DataName, DataSection


class Test(View):
    def get(self, request):
        context = {
            "sections": DataSection.objects.order_by("id"),
            "names": DataName.objects.filter(section_id=1).order_by("id"),
            "areas": Area.objects.all(),
        }

        return render(self.request, "index.html", context)

from datetime import date
from random import randint

from django.core.management.base import BaseCommand

from datastorage.models import Area, DataCriteria, DataName, DataValue


class Command(BaseCommand):
    def handle(self, *args, **options):
        DataValue.objects.all().delete()

        for area in Area.objects.all():
            for crit in DataCriteria.objects.all():
                for name in DataName.objects.all():
                    for year in [2021, 2022, 2023]:
                        for month in range(1, 13):
                            DataValue.objects.create(
                                area=area, criteria=crit, name=name, date=date(year, month, 1), value=randint(0, 100000)
                            )

from django.contrib import admin

from datastorage.models import DataCriteria, DataName, DataSection, DataValue, Area, DataCriteriaUnit

admin.site.register(DataValue)
admin.site.register(DataCriteria)
admin.site.register(DataName)
admin.site.register(DataSection)
admin.site.register(Area)
admin.site.register(DataCriteriaUnit)

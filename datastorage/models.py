from django.db import models


class DataSection(models.Model):
    name = models.CharField("Название", max_length=1024)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = verbose_name_plural = "Раздел данных"


class DataCriteriaUnit(models.Model):
    name = models.CharField("Название", max_length=1024)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = verbose_name_plural = "Единица измерения критерия данных"


class DataCriteria(models.Model):
    name = models.CharField("Название", max_length=1024)
    unit = models.ForeignKey(
        DataCriteriaUnit, models.CASCADE, "criteria", verbose_name="Единица измерения", null=True, blank=True
    )
    section = models.ForeignKey(DataSection, models.CASCADE, "criteria", verbose_name="Раздел")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = verbose_name_plural = "Критерий данных"


class DataName(models.Model):
    name = models.CharField("Название", max_length=1024)
    section = models.ForeignKey(DataSection, models.CASCADE, "names", verbose_name="Раздел")
    head = models.ForeignKey(
        "DataName", models.CASCADE, "sub_names", verbose_name="Старший название", null=True, blank=True
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = verbose_name_plural = "Название данных"


class Area(models.Model):
    name = models.CharField("Название", max_length=1024)
    head = models.ForeignKey("Area", models.CASCADE, "sub_areas", verbose_name="Старший", blank=True, null=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = verbose_name_plural = "География"


class DataValue(models.Model):
    value = models.FloatField("Значение")

    area = models.ForeignKey(Area, models.CASCADE, "values", verbose_name="Область")
    name = models.ForeignKey(DataName, models.CASCADE, "values", verbose_name="Название")
    criteria = models.ForeignKey(DataCriteria, models.CASCADE, "values", verbose_name="Критерий")

    def __str__(self):
        return f"{self.name} / {self.criteria} / {self.area} / {self.value}"

    class Meta:
        verbose_name = verbose_name_plural = "Значение"

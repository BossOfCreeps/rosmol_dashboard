# Generated by Django 4.1.7 on 2023-02-18 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("datastorage", "0003_alter_area_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="area",
            name="latitude",
            field=models.FloatField(blank=True, null=True, verbose_name="Широта"),
        ),
        migrations.AddField(
            model_name="area",
            name="longitude",
            field=models.FloatField(blank=True, null=True, verbose_name="Долгота"),
        ),
    ]

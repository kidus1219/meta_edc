# Generated by Django 3.2.11 on 2022-07-19 23:16

from django.db import migrations
from django.db.models import F


def update_egfr_drop_field_to_percent(apps, schema_editor):
    rft_model_cls = apps.get_model("meta_subject.historicalbloodresultsrft")
    rft_model_cls.objects.all().update(egfr_drop_value=F("egfr_drop_value") * 100)
    rft_model_cls = apps.get_model("meta_subject.bloodresultsrft")
    rft_model_cls.objects.all().update(egfr_drop_value=F("egfr_drop_value") * 100)


class Migration(migrations.Migration):
    dependencies = [
        ("meta_subject", "0129_auto_20220720_0108"),
    ]

    operations = [migrations.RunPython(update_egfr_drop_field_to_percent)]

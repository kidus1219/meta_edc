# Generated by Django 3.0.6 on 2020-06-13 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("meta_lists", "0008_auto_20200528_1517"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="MissedVisitReasons", new_name="SubjectVisitMissedReasons"
        )
    ]

# Generated by Django 3.2.7 on 2021-10-03 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("meta_prn", "0013_auto_20210911_2036"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="historicallosstofollowup",
            options={
                "get_latest_by": "history_date",
                "ordering": ("-history_date", "-history_id"),
                "verbose_name": "historical Loss to Follow Up",
            },
        ),
        migrations.AlterModelOptions(
            name="losstofollowup",
            options={
                "verbose_name": "Loss to Follow Up",
                "verbose_name_plural": "Loss to Follow Up",
            },
        ),
    ]
# Generated by Django 2.2.6 on 2019-11-07 19:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("meta_screening", "0014_auto_20191107_0528"),
    ]

    operations = [
        migrations.AddField(
            model_name="historicalscreeningpartone",
            name="refused",
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AddField(
            model_name="historicalscreeningpartthree",
            name="refused",
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AddField(
            model_name="historicalscreeningparttwo",
            name="refused",
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AddField(
            model_name="historicalsubjectscreening",
            name="refused",
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AddField(
            model_name="subjectscreening",
            name="refused",
            field=models.BooleanField(default=False, editable=False),
        ),
    ]

# Generated by Django 3.0.6 on 2020-05-28 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("meta_subject", "0042_auto_20200528_0252"),
    ]

    operations = [
        migrations.AddField(
            model_name="followup",
            name="symptoms_g3_detail",
            field=models.TextField(
                blank=True,
                null=True,
                verbose_name="Please provide details on any of the Grade 3 symptoms above.",
            ),
        ),
        migrations.AddField(
            model_name="followup",
            name="symptoms_g4_detail",
            field=models.TextField(
                blank=True,
                null=True,
                verbose_name="Please provide details on any of the Grade 4 symptoms above.",
            ),
        ),
        migrations.AddField(
            model_name="historicalfollowup",
            name="symptoms_g3_detail",
            field=models.TextField(
                blank=True,
                null=True,
                verbose_name="Please provide details on any of the Grade 3 symptoms above.",
            ),
        ),
        migrations.AddField(
            model_name="historicalfollowup",
            name="symptoms_g4_detail",
            field=models.TextField(
                blank=True,
                null=True,
                verbose_name="Please provide details on any of the Grade 4 symptoms above.",
            ),
        ),
    ]
# Generated by Django 3.2.11 on 2022-04-12 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("meta_consent", "0007_auto_20220128_1719"),
    ]

    operations = [
        migrations.AddField(
            model_name="historicalsubjectconsent",
            name="study_medication_name",
            field=models.CharField(
                default="metformin",
                editable=False,
                help_text="Used by `create_prescription` in the signal",
                max_length=25,
            ),
        ),
        migrations.AddField(
            model_name="subjectconsent",
            name="study_medication_name",
            field=models.CharField(
                default="metformin",
                editable=False,
                help_text="Used by `create_prescription` in the signal",
                max_length=25,
            ),
        ),
    ]
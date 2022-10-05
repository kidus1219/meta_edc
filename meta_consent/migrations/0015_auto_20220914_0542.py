# Generated by Django 3.2.13 on 2022-09-14 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("meta_consent", "0014_alter_subjectconsent_managers"),
    ]

    operations = [
        migrations.AddField(
            model_name="historicalsubjectconsent",
            name="ethnicity",
            field=models.CharField(
                editable=False, help_text="fromm screening", max_length=15, null=True
            ),
        ),
        migrations.AddField(
            model_name="subjectconsent",
            name="ethnicity",
            field=models.CharField(
                editable=False, help_text="fromm screening", max_length=15, null=True
            ),
        ),
    ]
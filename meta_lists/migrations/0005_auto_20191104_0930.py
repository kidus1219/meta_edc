# Generated by Django 2.2.6 on 2019-11-04 06:30

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [("meta_lists", "0004_auto_20191102_1859")]

    operations = [
        migrations.AlterModelOptions(
            name="arvregimens",
            options={
                "ordering": ["display_index", "display_name"],
                "verbose_name": "ARV Regimens",
                "verbose_name_plural": "ARV Regimens",
            },
        ),
        migrations.AlterModelOptions(
            name="baselinesymptoms",
            options={
                "ordering": ["display_index", "display_name"],
                "verbose_name": "Baseline Symptoms",
                "verbose_name_plural": "Baseline Symptoms",
            },
        ),
        migrations.AlterModelOptions(
            name="diabetessymptoms",
            options={
                "ordering": ["display_index", "display_name"],
                "verbose_name": "Diabetes Symptoms",
                "verbose_name_plural": "Diabetes Symptoms",
            },
        ),
        migrations.AlterModelOptions(
            name="hypertensionmedications",
            options={
                "ordering": ["display_index", "display_name"],
                "verbose_name": "Hypertension Medications",
                "verbose_name_plural": "Hypertension Medications",
            },
        ),
        migrations.AlterModelOptions(
            name="nonadherencereasons",
            options={
                "ordering": ["display_index", "display_name"],
                "verbose_name": "Non-Adherence Reasons",
                "verbose_name_plural": "Non-Adherence Reasons",
            },
        ),
        migrations.AlterModelOptions(
            name="offstudyreasons",
            options={
                "ordering": ["display_index", "display_name"],
                "verbose_name": "Offstudy Reasons",
                "verbose_name_plural": "Offstudy Reasons",
            },
        ),
        migrations.AlterModelOptions(
            name="oiprophylaxis",
            options={
                "ordering": ["display_index", "display_name"],
                "verbose_name": "OI Prophylaxis",
                "verbose_name_plural": "OI Prophylaxis",
            },
        ),
        migrations.AlterModelOptions(
            name="symptoms",
            options={
                "ordering": ["display_index", "display_name"],
                "verbose_name": "Symptoms",
                "verbose_name_plural": "Symptoms",
            },
        ),
    ]

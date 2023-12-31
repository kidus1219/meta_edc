# Generated by Django 4.0.5 on 2022-06-29 17:26

import django.contrib.sites.managers
from django.db import migrations, models
import edc_visit_tracking.managers


class Migration(migrations.Migration):
    dependencies = [
        ("meta_subject", "0116_egfrnotification_report_status_and_more"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="egfrnotification",
            managers=[
                ("on_site", django.contrib.sites.managers.CurrentSiteManager()),
                ("objects", edc_visit_tracking.managers.CrfModelManager()),
            ],
        ),
        migrations.AddField(
            model_name="egfrnotification",
            name="crf_status",
            field=models.CharField(
                choices=[
                    ("INCOMPLETE", "Incomplete (some data pending)"),
                    ("COMPLETE", "Complete"),
                ],
                default="COMPLETE",
                help_text="If some data is still pending, flag this CRF as incomplete",
                max_length=25,
                verbose_name="CRF status",
            ),
        ),
        migrations.AddField(
            model_name="egfrnotification",
            name="crf_status_comments",
            field=models.TextField(
                blank=True,
                help_text="for example, why some data is still pending",
                null=True,
                verbose_name="Any comments related to status of this CRF",
            ),
        ),
        migrations.AddField(
            model_name="historicalegfrnotification",
            name="crf_status",
            field=models.CharField(
                choices=[
                    ("INCOMPLETE", "Incomplete (some data pending)"),
                    ("COMPLETE", "Complete"),
                ],
                default="COMPLETE",
                help_text="If some data is still pending, flag this CRF as incomplete",
                max_length=25,
                verbose_name="CRF status",
            ),
        ),
        migrations.AddField(
            model_name="historicalegfrnotification",
            name="crf_status_comments",
            field=models.TextField(
                blank=True,
                help_text="for example, why some data is still pending",
                null=True,
                verbose_name="Any comments related to status of this CRF",
            ),
        ),
        migrations.AlterField(
            model_name="egfrnotification",
            name="egfr_percent_change",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                help_text="Copied from RFT result eGFR section",
                max_digits=10,
                null=True,
                verbose_name="Change from baseline",
            ),
        ),
        migrations.AlterField(
            model_name="historicalegfrnotification",
            name="egfr_percent_change",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                help_text="Copied from RFT result eGFR section",
                max_digits=10,
                null=True,
                verbose_name="Change from baseline",
            ),
        ),
    ]

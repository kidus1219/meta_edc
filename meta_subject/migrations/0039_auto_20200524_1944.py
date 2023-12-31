# Generated by Django 3.0.6 on 2020-05-24 16:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("meta_subject", "0038_auto_20200520_0020"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bloodresultsglu",
            name="glucose_units",
            field=models.CharField(
                blank=True,
                choices=[("mg/dL", "mg/dL"), ("mmol/L", "mmol/L (millimoles/L)")],
                max_length=15,
                null=True,
                verbose_name="units",
            ),
        ),
        migrations.AlterField(
            model_name="bloodresultsrft",
            name="creatinine_units",
            field=models.CharField(
                blank=True,
                choices=[("mg/dL", "mg/dL"), ("umol/L", "μmol/L (micromoles/L)")],
                max_length=15,
                null=True,
                verbose_name="Units (creatinine)",
            ),
        ),
        migrations.AlterField(
            model_name="bloodresultsrft",
            name="uric_acid_units",
            field=models.CharField(
                blank=True,
                choices=[("mmol/L", "mmol/L (millimoles/L)"), ("mg/dL", "mg/dL")],
                max_length=15,
                null=True,
                verbose_name="units",
            ),
        ),
        migrations.AlterField(
            model_name="glucose",
            name="fasting_glucose_units",
            field=models.CharField(
                blank=True,
                choices=[("mg/dL", "mg/dL"), ("mmol/L", "mmol/L (millimoles/L)")],
                max_length=15,
                null=True,
                verbose_name="Units (fasting glucose)",
            ),
        ),
        migrations.AlterField(
            model_name="glucose",
            name="ogtt_two_hr_units",
            field=models.CharField(
                blank=True,
                choices=[("mg/dL", "mg/dL"), ("mmol/L", "mmol/L (millimoles/L)")],
                max_length=15,
                null=True,
                verbose_name="Units (Blood glucose 2hrs after...)",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbloodresultsglu",
            name="glucose_units",
            field=models.CharField(
                blank=True,
                choices=[("mg/dL", "mg/dL"), ("mmol/L", "mmol/L (millimoles/L)")],
                max_length=15,
                null=True,
                verbose_name="units",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbloodresultsrft",
            name="creatinine_units",
            field=models.CharField(
                blank=True,
                choices=[("mg/dL", "mg/dL"), ("umol/L", "μmol/L (micromoles/L)")],
                max_length=15,
                null=True,
                verbose_name="Units (creatinine)",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbloodresultsrft",
            name="uric_acid_units",
            field=models.CharField(
                blank=True,
                choices=[("mmol/L", "mmol/L (millimoles/L)"), ("mg/dL", "mg/dL")],
                max_length=15,
                null=True,
                verbose_name="units",
            ),
        ),
        migrations.AlterField(
            model_name="historicalglucose",
            name="fasting_glucose_units",
            field=models.CharField(
                blank=True,
                choices=[("mg/dL", "mg/dL"), ("mmol/L", "mmol/L (millimoles/L)")],
                max_length=15,
                null=True,
                verbose_name="Units (fasting glucose)",
            ),
        ),
        migrations.AlterField(
            model_name="historicalglucose",
            name="ogtt_two_hr_units",
            field=models.CharField(
                blank=True,
                choices=[("mg/dL", "mg/dL"), ("mmol/L", "mmol/L (millimoles/L)")],
                max_length=15,
                null=True,
                verbose_name="Units (Blood glucose 2hrs after...)",
            ),
        ),
        migrations.AlterField(
            model_name="historicalsubjectvisit",
            name="info_source",
            field=models.CharField(
                choices=[
                    ("hospital_notes", "Hospital notes"),
                    ("outpatient_cards", "Outpatient cards"),
                    ("patient", "Patient"),
                    ("collateral_history", "Collateral History from relative/guardian"),
                    ("N/A", "Not applicable (if missed)"),
                    ("OTHER", "Other"),
                ],
                max_length=25,
                verbose_name="What is the main source of this information?",
            ),
        ),
        migrations.AlterField(
            model_name="historicalsubjectvisit",
            name="reason",
            field=models.CharField(
                choices=[
                    ("scheduled", "Scheduled visit"),
                    ("unscheduled", "Unscheduled visit"),
                    ("missed", "Missed visit"),
                ],
                help_text="If 'missed', fill in the separate missed visit report",
                max_length=25,
                verbose_name="What is the reason for this visit report?",
            ),
        ),
        migrations.AlterField(
            model_name="subjectvisit",
            name="info_source",
            field=models.CharField(
                choices=[
                    ("hospital_notes", "Hospital notes"),
                    ("outpatient_cards", "Outpatient cards"),
                    ("patient", "Patient"),
                    ("collateral_history", "Collateral History from relative/guardian"),
                    ("N/A", "Not applicable (if missed)"),
                    ("OTHER", "Other"),
                ],
                max_length=25,
                verbose_name="What is the main source of this information?",
            ),
        ),
        migrations.AlterField(
            model_name="subjectvisit",
            name="reason",
            field=models.CharField(
                choices=[
                    ("scheduled", "Scheduled visit"),
                    ("unscheduled", "Unscheduled visit"),
                    ("missed", "Missed visit"),
                ],
                help_text="If 'missed', fill in the separate missed visit report",
                max_length=25,
                verbose_name="What is the reason for this visit report?",
            ),
        ),
    ]

# Generated by Django 4.2 on 2022-08-15 15:33

import django.core.validators
from django.db import migrations, models
import edc_model.validators.date
import edc_protocol.validators
import edc_utils.date
import edc_vitals.models.fields.weight


class Migration(migrations.Migration):

    dependencies = [
        ("meta_subject", "0135_auto_20220722_2212"),
    ]

    operations = [
        migrations.AddField(
            model_name="egfrdropnotification",
            name="creatinine_quantifier",
            field=models.CharField(
                blank=True,
                choices=[("=", "="), (">", ">"), (">=", ">="), ("<", "<"), ("<=", "<=")],
                default="=",
                max_length=10,
                null=True,
                verbose_name="Quantifier",
            ),
        ),
        migrations.AddField(
            model_name="egfrdropnotification",
            name="egfr_quantifier",
            field=models.CharField(
                blank=True,
                choices=[("=", "="), (">", ">"), (">=", ">="), ("<", "<"), ("<=", "<=")],
                default="=",
                max_length=10,
                null=True,
                verbose_name="Quantifier",
            ),
        ),
        migrations.AddField(
            model_name="egfrdropnotification",
            name="egfr_units",
            field=models.CharField(
                blank=True,
                choices=[("mL/min/1.73m2", "mL/min/1.73m2")],
                default="mL/min/1.73m2",
                max_length=15,
                null=True,
                verbose_name="units",
            ),
        ),
        migrations.AddField(
            model_name="egfrdropnotification",
            name="egfr_value",
            field=models.DecimalField(
                blank=True,
                decimal_places=4,
                max_digits=8,
                null=True,
                validators=[django.core.validators.MinValueValidator(0.0)],
                verbose_name="eGFR",
            ),
        ),
        migrations.AddField(
            model_name="egfrdropnotification",
            name="weight",
            field=edc_vitals.models.fields.weight.WeightField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="historicalegfrdropnotification",
            name="creatinine_quantifier",
            field=models.CharField(
                blank=True,
                choices=[("=", "="), (">", ">"), (">=", ">="), ("<", "<"), ("<=", "<=")],
                default="=",
                max_length=10,
                null=True,
                verbose_name="Quantifier",
            ),
        ),
        migrations.AddField(
            model_name="historicalegfrdropnotification",
            name="egfr_quantifier",
            field=models.CharField(
                blank=True,
                choices=[("=", "="), (">", ">"), (">=", ">="), ("<", "<"), ("<=", "<=")],
                default="=",
                max_length=10,
                null=True,
                verbose_name="Quantifier",
            ),
        ),
        migrations.AddField(
            model_name="historicalegfrdropnotification",
            name="egfr_units",
            field=models.CharField(
                blank=True,
                choices=[("mL/min/1.73m2", "mL/min/1.73m2")],
                default="mL/min/1.73m2",
                max_length=15,
                null=True,
                verbose_name="units",
            ),
        ),
        migrations.AddField(
            model_name="historicalegfrdropnotification",
            name="egfr_value",
            field=models.DecimalField(
                blank=True,
                decimal_places=4,
                max_digits=8,
                null=True,
                validators=[django.core.validators.MinValueValidator(0.0)],
                verbose_name="eGFR",
            ),
        ),
        migrations.AddField(
            model_name="historicalegfrdropnotification",
            name="weight",
            field=edc_vitals.models.fields.weight.WeightField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="egfrdropnotification",
            name="creatinine_date",
            field=models.DateField(verbose_name="Serum creatinine date"),
        ),
        migrations.AlterField(
            model_name="egfrdropnotification",
            name="creatinine_units",
            field=models.CharField(
                blank=True,
                choices=[
                    (
                        (("mg/dL", "mg/dL"), ("umol/L", "μmol/L (micromoles/L)")),
                        (("mg/dL", "mg/dL"), ("umol/L", "μmol/L (micromoles/L)")),
                    )
                ],
                default="umol/L",
                max_length=15,
                null=True,
                verbose_name="units",
            ),
        ),
        migrations.AlterField(
            model_name="egfrdropnotification",
            name="creatinine_value",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=8,
                null=True,
                validators=[django.core.validators.MinValueValidator(0.0)],
                verbose_name="Serum creatinine",
            ),
        ),
        migrations.AlterField(
            model_name="egfrdropnotification",
            name="report_datetime",
            field=models.DateTimeField(
                default=edc_utils.date.get_utcnow,
                help_text="If reporting today, use today's date/time, otherwise use the date/time this information was reported.",
                validators=[
                    edc_protocol.validators.datetime_not_before_study_start,
                    edc_model.validators.date.datetime_not_future,
                ],
                verbose_name="Report Date",
            ),
        ),
        migrations.AlterField(
            model_name="egfrdropnotification",
            name="report_status",
            field=models.CharField(
                choices=[
                    ("open", "Open. Some information is still pending."),
                    ("closed", "Closed. This report is complete"),
                ],
                default="New",
                max_length=15,
            ),
        ),
        migrations.AlterField(
            model_name="historicalegfrdropnotification",
            name="creatinine_date",
            field=models.DateField(verbose_name="Serum creatinine date"),
        ),
        migrations.AlterField(
            model_name="historicalegfrdropnotification",
            name="creatinine_units",
            field=models.CharField(
                blank=True,
                choices=[
                    (
                        (("mg/dL", "mg/dL"), ("umol/L", "μmol/L (micromoles/L)")),
                        (("mg/dL", "mg/dL"), ("umol/L", "μmol/L (micromoles/L)")),
                    )
                ],
                default="umol/L",
                max_length=15,
                null=True,
                verbose_name="units",
            ),
        ),
        migrations.AlterField(
            model_name="historicalegfrdropnotification",
            name="creatinine_value",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=8,
                null=True,
                validators=[django.core.validators.MinValueValidator(0.0)],
                verbose_name="Serum creatinine",
            ),
        ),
        migrations.AlterField(
            model_name="historicalegfrdropnotification",
            name="report_datetime",
            field=models.DateTimeField(
                default=edc_utils.date.get_utcnow,
                help_text="If reporting today, use today's date/time, otherwise use the date/time this information was reported.",
                validators=[
                    edc_protocol.validators.datetime_not_before_study_start,
                    edc_model.validators.date.datetime_not_future,
                ],
                verbose_name="Report Date",
            ),
        ),
        migrations.AlterField(
            model_name="historicalegfrdropnotification",
            name="report_status",
            field=models.CharField(
                choices=[
                    ("open", "Open. Some information is still pending."),
                    ("closed", "Closed. This report is complete"),
                ],
                default="New",
                max_length=15,
            ),
        ),
    ]

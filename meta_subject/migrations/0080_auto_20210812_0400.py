# Generated by Django 3.2.4 on 2021-08-12 01:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("meta_subject", "0079_auto_20210812_0335"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bloodresultsfbc",
            name="haemoglobin_value",
            field=models.DecimalField(
                blank=True,
                decimal_places=1,
                max_digits=6,
                null=True,
                validators=[django.core.validators.MinValueValidator(0.0)],
                verbose_name="Haemoglobin",
            ),
        ),
        migrations.AlterField(
            model_name="bloodresultsfbc",
            name="mch_value",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=6,
                null=True,
                validators=[django.core.validators.MinValueValidator(0.0)],
                verbose_name="MCH",
            ),
        ),
        migrations.AlterField(
            model_name="bloodresultsfbc",
            name="mchc_value",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=6,
                null=True,
                validators=[django.core.validators.MinValueValidator(0.0)],
                verbose_name="MCHC",
            ),
        ),
        migrations.AlterField(
            model_name="bloodresultsfbc",
            name="mcv_value",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=6,
                null=True,
                validators=[django.core.validators.MinValueValidator(0.0)],
                verbose_name="MCV",
            ),
        ),
        migrations.AlterField(
            model_name="bloodresultsfbc",
            name="platelets_value",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=6,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(1.0),
                    django.core.validators.MaxValueValidator(9999.0),
                ],
                verbose_name="Platelets",
            ),
        ),
        migrations.AlterField(
            model_name="bloodresultsfbc",
            name="wbc_value",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=6,
                null=True,
                validators=[django.core.validators.MinValueValidator(0.0)],
                verbose_name="WBC",
            ),
        ),
        migrations.AlterField(
            model_name="bloodresultslft",
            name="albumin_value",
            field=models.DecimalField(
                blank=True,
                decimal_places=1,
                max_digits=6,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(1.0),
                    django.core.validators.MaxValueValidator(999.0),
                ],
                verbose_name="Serum albumin",
            ),
        ),
        migrations.AlterField(
            model_name="bloodresultslft",
            name="alp_value",
            field=models.DecimalField(
                blank=True,
                decimal_places=1,
                max_digits=6,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(1.0),
                    django.core.validators.MaxValueValidator(999.0),
                ],
                verbose_name="ALP",
            ),
        ),
        migrations.AlterField(
            model_name="bloodresultslft",
            name="alt_value",
            field=models.DecimalField(
                blank=True,
                decimal_places=1,
                max_digits=6,
                null=True,
                validators=[django.core.validators.MinValueValidator(0.0)],
                verbose_name="ALT",
            ),
        ),
        migrations.AlterField(
            model_name="bloodresultslft",
            name="amylase_value",
            field=models.DecimalField(
                blank=True,
                decimal_places=1,
                max_digits=6,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(1.0),
                    django.core.validators.MaxValueValidator(999.0),
                ],
                verbose_name="Serum Amylase",
            ),
        ),
        migrations.AlterField(
            model_name="bloodresultslft",
            name="ast_value",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=6,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(1.0),
                    django.core.validators.MaxValueValidator(999.0),
                ],
                verbose_name="AST",
            ),
        ),
        migrations.AlterField(
            model_name="bloodresultslft",
            name="ggt_value",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=6,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(1.0),
                    django.core.validators.MaxValueValidator(999.0),
                ],
                verbose_name="GGT",
            ),
        ),
        migrations.AlterField(
            model_name="bloodresultslipid",
            name="chol_value",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=8,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(0.0),
                    django.core.validators.MaxValueValidator(999.0),
                ],
                verbose_name="Total Cholesterol",
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
                verbose_name="units",
            ),
        ),
        migrations.AlterField(
            model_name="bloodresultsrft",
            name="creatinine_value",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=6,
                null=True,
                validators=[django.core.validators.MinValueValidator(0.0)],
                verbose_name="Creatinine",
            ),
        ),
        migrations.AlterField(
            model_name="bloodresultsrft",
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
        migrations.AlterField(
            model_name="bloodresultsrft",
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
        migrations.AlterField(
            model_name="bloodresultsrft",
            name="urea_value",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=6,
                null=True,
                validators=[django.core.validators.MinValueValidator(0.0)],
                verbose_name="Urea (BUN)",
            ),
        ),
        migrations.AlterField(
            model_name="bloodresultsrft",
            name="uric_acid_value",
            field=models.DecimalField(
                blank=True,
                decimal_places=4,
                max_digits=10,
                null=True,
                validators=[django.core.validators.MinValueValidator(0.0)],
                verbose_name="Uric Acid",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbloodresultsfbc",
            name="haemoglobin_value",
            field=models.DecimalField(
                blank=True,
                decimal_places=1,
                max_digits=6,
                null=True,
                validators=[django.core.validators.MinValueValidator(0.0)],
                verbose_name="Haemoglobin",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbloodresultsfbc",
            name="mch_value",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=6,
                null=True,
                validators=[django.core.validators.MinValueValidator(0.0)],
                verbose_name="MCH",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbloodresultsfbc",
            name="mchc_value",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=6,
                null=True,
                validators=[django.core.validators.MinValueValidator(0.0)],
                verbose_name="MCHC",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbloodresultsfbc",
            name="mcv_value",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=6,
                null=True,
                validators=[django.core.validators.MinValueValidator(0.0)],
                verbose_name="MCV",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbloodresultsfbc",
            name="platelets_value",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=6,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(1.0),
                    django.core.validators.MaxValueValidator(9999.0),
                ],
                verbose_name="Platelets",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbloodresultsfbc",
            name="wbc_value",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=6,
                null=True,
                validators=[django.core.validators.MinValueValidator(0.0)],
                verbose_name="WBC",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbloodresultslft",
            name="albumin_value",
            field=models.DecimalField(
                blank=True,
                decimal_places=1,
                max_digits=6,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(1.0),
                    django.core.validators.MaxValueValidator(999.0),
                ],
                verbose_name="Serum albumin",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbloodresultslft",
            name="alp_value",
            field=models.DecimalField(
                blank=True,
                decimal_places=1,
                max_digits=6,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(1.0),
                    django.core.validators.MaxValueValidator(999.0),
                ],
                verbose_name="ALP",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbloodresultslft",
            name="alt_value",
            field=models.DecimalField(
                blank=True,
                decimal_places=1,
                max_digits=6,
                null=True,
                validators=[django.core.validators.MinValueValidator(0.0)],
                verbose_name="ALT",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbloodresultslft",
            name="amylase_value",
            field=models.DecimalField(
                blank=True,
                decimal_places=1,
                max_digits=6,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(1.0),
                    django.core.validators.MaxValueValidator(999.0),
                ],
                verbose_name="Serum Amylase",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbloodresultslft",
            name="ast_value",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=6,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(1.0),
                    django.core.validators.MaxValueValidator(999.0),
                ],
                verbose_name="AST",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbloodresultslft",
            name="ggt_value",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=6,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(1.0),
                    django.core.validators.MaxValueValidator(999.0),
                ],
                verbose_name="GGT",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbloodresultslipid",
            name="chol_value",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=8,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(0.0),
                    django.core.validators.MaxValueValidator(999.0),
                ],
                verbose_name="Total Cholesterol",
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
                verbose_name="units",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbloodresultsrft",
            name="creatinine_value",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=6,
                null=True,
                validators=[django.core.validators.MinValueValidator(0.0)],
                verbose_name="Creatinine",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbloodresultsrft",
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
        migrations.AlterField(
            model_name="historicalbloodresultsrft",
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
        migrations.AlterField(
            model_name="historicalbloodresultsrft",
            name="urea_value",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=6,
                null=True,
                validators=[django.core.validators.MinValueValidator(0.0)],
                verbose_name="Urea (BUN)",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbloodresultsrft",
            name="uric_acid_value",
            field=models.DecimalField(
                blank=True,
                decimal_places=4,
                max_digits=10,
                null=True,
                validators=[django.core.validators.MinValueValidator(0.0)],
                verbose_name="Uric Acid",
            ),
        ),
    ]
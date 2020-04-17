# Generated by Django 2.2.7 on 2019-11-14 22:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("meta_subject", "0007_auto_20191107_2249"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bloodresultsfbc",
            name="haemoglobin_units",
            field=models.CharField(
                blank=True,
                choices=[("g/dL", "g/dL")],
                max_length=15,
                null=True,
                verbose_name="units",
            ),
        ),
        migrations.AlterField(
            model_name="bloodresultsfbc",
            name="hct",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=6,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(1.0),
                    django.core.validators.MaxValueValidator(999.0),
                ],
                verbose_name="Hematocrit",
            ),
        ),
        migrations.AlterField(
            model_name="bloodresultsfbc",
            name="hct_units",
            field=models.CharField(
                blank=True,
                choices=[("%", "%")],
                max_length=15,
                null=True,
                verbose_name="units",
            ),
        ),
        migrations.AlterField(
            model_name="bloodresultsfbc",
            name="platelets_units",
            field=models.CharField(
                blank=True,
                choices=[("10^9/L", "10^9/L"), ("cells/mm^3", "cells/mm<sup>3</sup>")],
                max_length=15,
                null=True,
                verbose_name="units",
            ),
        ),
        migrations.AlterField(
            model_name="bloodresultsfbc",
            name="rbc_units",
            field=models.CharField(
                blank=True,
                choices=[("10^9/L", "10^9/L"), ("cells/mm^3", "cells/mm^3")],
                max_length=15,
                null=True,
                verbose_name="units",
            ),
        ),
        migrations.AlterField(
            model_name="bloodresultsfbc",
            name="wbc_units",
            field=models.CharField(
                blank=True,
                choices=[("10^9/L", "10^9/L"), ("cells/mm^3", "cells/mm<sup>3</sup>")],
                max_length=15,
                null=True,
                verbose_name="units",
            ),
        ),
        migrations.AlterField(
            model_name="bloodresultsglu",
            name="glucose_units",
            field=models.CharField(
                blank=True,
                choices=[("mg/dL", "mg/dL"), ("mmol/L", "mmol/L")],
                max_length=15,
                null=True,
                verbose_name="units",
            ),
        ),
        migrations.AlterField(
            model_name="bloodresultshba1c",
            name="hba1c_units",
            field=models.CharField(
                blank=True,
                choices=[("%", "%")],
                max_length=15,
                null=True,
                verbose_name="units",
            ),
        ),
        migrations.AlterField(
            model_name="bloodresultslft",
            name="albumin_units",
            field=models.CharField(
                blank=True,
                choices=[("g/dL", "g/dL"), ("g/L", "g/L")],
                max_length=15,
                null=True,
                verbose_name="units",
            ),
        ),
        migrations.AlterField(
            model_name="bloodresultslft",
            name="alp_units",
            field=models.CharField(
                blank=True,
                choices=[("IU/L", "U/L")],
                max_length=15,
                null=True,
                verbose_name="units",
            ),
        ),
        migrations.AlterField(
            model_name="bloodresultslft",
            name="alt_units",
            field=models.CharField(
                blank=True,
                choices=[("IU/L", "U/L")],
                max_length=15,
                null=True,
                verbose_name="units",
            ),
        ),
        migrations.AlterField(
            model_name="bloodresultslft",
            name="amylase_units",
            field=models.CharField(
                blank=True,
                choices=[("IU/L", "U/L")],
                max_length=15,
                null=True,
                verbose_name="units",
            ),
        ),
        migrations.AlterField(
            model_name="bloodresultslft",
            name="ast_units",
            field=models.CharField(
                blank=True,
                choices=[("IU/L", "U/L")],
                max_length=15,
                null=True,
                verbose_name="units",
            ),
        ),
        migrations.AlterField(
            model_name="bloodresultslft",
            name="ggt_units",
            field=models.CharField(
                blank=True,
                choices=[("IU/L", "U/L")],
                max_length=15,
                null=True,
                verbose_name="units",
            ),
        ),
        migrations.AlterField(
            model_name="bloodresultsrft",
            name="creatinine",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=8,
                null=True,
                verbose_name="Creatinine <u>level</u>",
            ),
        ),
        migrations.AlterField(
            model_name="bloodresultsrft",
            name="creatinine_units",
            field=models.CharField(
                blank=True,
                choices=[("mg/dL", "mg/dL"), ("umol/L", "μmol/L")],
                max_length=15,
                null=True,
                verbose_name="Units (creatinine)",
            ),
        ),
        migrations.AlterField(
            model_name="bloodresultsrft",
            name="urea_units",
            field=models.CharField(
                blank=True,
                choices=[("mmol/L", "mmol/L")],
                max_length=15,
                null=True,
                verbose_name="units",
            ),
        ),
        migrations.AlterField(
            model_name="bloodresultsrft",
            name="uric_acid",
            field=models.DecimalField(
                blank=True,
                decimal_places=4,
                max_digits=10,
                null=True,
                verbose_name="Uric Acid",
            ),
        ),
        migrations.AlterField(
            model_name="bloodresultsrft",
            name="uric_acid_units",
            field=models.CharField(
                blank=True,
                choices=[("mg/dL", "mg/dL")],
                max_length=15,
                null=True,
                verbose_name="units",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbloodresultsfbc",
            name="haemoglobin_units",
            field=models.CharField(
                blank=True,
                choices=[("g/dL", "g/dL")],
                max_length=15,
                null=True,
                verbose_name="units",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbloodresultsfbc",
            name="hct",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=6,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(1.0),
                    django.core.validators.MaxValueValidator(999.0),
                ],
                verbose_name="Hematocrit",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbloodresultsfbc",
            name="hct_units",
            field=models.CharField(
                blank=True,
                choices=[("%", "%")],
                max_length=15,
                null=True,
                verbose_name="units",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbloodresultsfbc",
            name="platelets_units",
            field=models.CharField(
                blank=True,
                choices=[("10^9/L", "10^9/L"), ("cells/mm^3", "cells/mm<sup>3</sup>")],
                max_length=15,
                null=True,
                verbose_name="units",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbloodresultsfbc",
            name="rbc_units",
            field=models.CharField(
                blank=True,
                choices=[("10^9/L", "10^9/L"), ("cells/mm^3", "cells/mm^3")],
                max_length=15,
                null=True,
                verbose_name="units",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbloodresultsfbc",
            name="wbc_units",
            field=models.CharField(
                blank=True,
                choices=[("10^9/L", "10^9/L"), ("cells/mm^3", "cells/mm<sup>3</sup>")],
                max_length=15,
                null=True,
                verbose_name="units",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbloodresultsglu",
            name="glucose_units",
            field=models.CharField(
                blank=True,
                choices=[("mg/dL", "mg/dL"), ("mmol/L", "mmol/L")],
                max_length=15,
                null=True,
                verbose_name="units",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbloodresultshba1c",
            name="hba1c_units",
            field=models.CharField(
                blank=True,
                choices=[("%", "%")],
                max_length=15,
                null=True,
                verbose_name="units",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbloodresultslft",
            name="albumin_units",
            field=models.CharField(
                blank=True,
                choices=[("g/dL", "g/dL"), ("g/L", "g/L")],
                max_length=15,
                null=True,
                verbose_name="units",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbloodresultslft",
            name="alp_units",
            field=models.CharField(
                blank=True,
                choices=[("IU/L", "U/L")],
                max_length=15,
                null=True,
                verbose_name="units",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbloodresultslft",
            name="alt_units",
            field=models.CharField(
                blank=True,
                choices=[("IU/L", "U/L")],
                max_length=15,
                null=True,
                verbose_name="units",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbloodresultslft",
            name="amylase_units",
            field=models.CharField(
                blank=True,
                choices=[("IU/L", "U/L")],
                max_length=15,
                null=True,
                verbose_name="units",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbloodresultslft",
            name="ast_units",
            field=models.CharField(
                blank=True,
                choices=[("IU/L", "U/L")],
                max_length=15,
                null=True,
                verbose_name="units",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbloodresultslft",
            name="ggt_units",
            field=models.CharField(
                blank=True,
                choices=[("IU/L", "U/L")],
                max_length=15,
                null=True,
                verbose_name="units",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbloodresultsrft",
            name="creatinine",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=8,
                null=True,
                verbose_name="Creatinine <u>level</u>",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbloodresultsrft",
            name="creatinine_units",
            field=models.CharField(
                blank=True,
                choices=[("mg/dL", "mg/dL"), ("umol/L", "μmol/L")],
                max_length=15,
                null=True,
                verbose_name="Units (creatinine)",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbloodresultsrft",
            name="urea_units",
            field=models.CharField(
                blank=True,
                choices=[("mmol/L", "mmol/L")],
                max_length=15,
                null=True,
                verbose_name="units",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbloodresultsrft",
            name="uric_acid",
            field=models.DecimalField(
                blank=True,
                decimal_places=4,
                max_digits=10,
                null=True,
                verbose_name="Uric Acid",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbloodresultsrft",
            name="uric_acid_units",
            field=models.CharField(
                blank=True,
                choices=[("mg/dL", "mg/dL")],
                max_length=15,
                null=True,
                verbose_name="units",
            ),
        ),
    ]
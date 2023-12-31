# Generated by Django 3.2.11 on 2022-03-12 16:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("meta_screening", "0038_auto_20220312_1929"),
    ]

    operations = [
        migrations.AlterField(
            model_name="historicalicpreferral",
            name="fbg_value",
            field=models.DecimalField(
                decimal_places=4,
                help_text="mmol/L",
                max_digits=8,
                null=True,
                verbose_name="FBG level",
            ),
        ),
        migrations.AlterField(
            model_name="historicalscreeningpartone",
            name="converted_fbg2_value",
            field=models.DecimalField(
                decimal_places=4,
                help_text="mmol/L (system converted)",
                max_digits=8,
                null=True,
                verbose_name="REPEAT FBG level",
            ),
        ),
        migrations.AlterField(
            model_name="historicalscreeningpartone",
            name="converted_fbg_value",
            field=models.DecimalField(
                decimal_places=4,
                help_text="mmol/L (system converted)",
                max_digits=8,
                null=True,
                verbose_name="FBG level",
            ),
        ),
        migrations.AlterField(
            model_name="historicalscreeningpartone",
            name="fbg2_units",
            field=models.CharField(
                blank=True,
                choices=[("mg/dL", "mg/dL"), ("mmol/L", "mmol/L (millimoles/L)")],
                max_length=15,
                null=True,
                verbose_name="FBG units",
            ),
        ),
        migrations.AlterField(
            model_name="historicalscreeningpartthree",
            name="converted_fbg2_value",
            field=models.DecimalField(
                decimal_places=4,
                help_text="mmol/L (system converted)",
                max_digits=8,
                null=True,
                verbose_name="REPEAT FBG level",
            ),
        ),
        migrations.AlterField(
            model_name="historicalscreeningpartthree",
            name="converted_fbg_value",
            field=models.DecimalField(
                decimal_places=4,
                help_text="mmol/L (system converted)",
                max_digits=8,
                null=True,
                verbose_name="FBG level",
            ),
        ),
        migrations.AlterField(
            model_name="historicalscreeningpartthree",
            name="fbg2_units",
            field=models.CharField(
                blank=True,
                choices=[("mg/dL", "mg/dL"), ("mmol/L", "mmol/L (millimoles/L)")],
                max_length=15,
                null=True,
                verbose_name="FBG units",
            ),
        ),
        migrations.AlterField(
            model_name="historicalscreeningparttwo",
            name="converted_fbg2_value",
            field=models.DecimalField(
                decimal_places=4,
                help_text="mmol/L (system converted)",
                max_digits=8,
                null=True,
                verbose_name="REPEAT FBG level",
            ),
        ),
        migrations.AlterField(
            model_name="historicalscreeningparttwo",
            name="converted_fbg_value",
            field=models.DecimalField(
                decimal_places=4,
                help_text="mmol/L (system converted)",
                max_digits=8,
                null=True,
                verbose_name="FBG level",
            ),
        ),
        migrations.AlterField(
            model_name="historicalscreeningparttwo",
            name="fbg2_units",
            field=models.CharField(
                blank=True,
                choices=[("mg/dL", "mg/dL"), ("mmol/L", "mmol/L (millimoles/L)")],
                max_length=15,
                null=True,
                verbose_name="FBG units",
            ),
        ),
        migrations.AlterField(
            model_name="historicalsubjectscreening",
            name="converted_fbg2_value",
            field=models.DecimalField(
                decimal_places=4,
                help_text="mmol/L (system converted)",
                max_digits=8,
                null=True,
                verbose_name="REPEAT FBG level",
            ),
        ),
        migrations.AlterField(
            model_name="historicalsubjectscreening",
            name="converted_fbg_value",
            field=models.DecimalField(
                decimal_places=4,
                help_text="mmol/L (system converted)",
                max_digits=8,
                null=True,
                verbose_name="FBG level",
            ),
        ),
        migrations.AlterField(
            model_name="historicalsubjectscreening",
            name="fbg2_units",
            field=models.CharField(
                blank=True,
                choices=[("mg/dL", "mg/dL"), ("mmol/L", "mmol/L (millimoles/L)")],
                max_length=15,
                null=True,
                verbose_name="FBG units",
            ),
        ),
        migrations.AlterField(
            model_name="icpreferral",
            name="fbg_value",
            field=models.DecimalField(
                decimal_places=4,
                help_text="mmol/L",
                max_digits=8,
                null=True,
                verbose_name="FBG level",
            ),
        ),
        migrations.AlterField(
            model_name="subjectscreening",
            name="converted_fbg2_value",
            field=models.DecimalField(
                decimal_places=4,
                help_text="mmol/L (system converted)",
                max_digits=8,
                null=True,
                verbose_name="REPEAT FBG level",
            ),
        ),
        migrations.AlterField(
            model_name="subjectscreening",
            name="converted_fbg_value",
            field=models.DecimalField(
                decimal_places=4,
                help_text="mmol/L (system converted)",
                max_digits=8,
                null=True,
                verbose_name="FBG level",
            ),
        ),
        migrations.AlterField(
            model_name="subjectscreening",
            name="fbg2_units",
            field=models.CharField(
                blank=True,
                choices=[("mg/dL", "mg/dL"), ("mmol/L", "mmol/L (millimoles/L)")],
                max_length=15,
                null=True,
                verbose_name="FBG units",
            ),
        ),
    ]

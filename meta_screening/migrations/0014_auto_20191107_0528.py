# Generated by Django 2.2.6 on 2019-11-07 02:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("meta_screening", "0013_auto_20191107_0442")]

    operations = [
        migrations.AlterField(
            model_name="historicalscreeningpartone",
            name="converted_ogtt_two_hr",
            field=models.DecimalField(
                decimal_places=4,
                help_text="mmol/L (system converted)",
                max_digits=8,
                null=True,
                verbose_name="Blood glucose level 2-hours",
            ),
        ),
        migrations.AlterField(
            model_name="historicalscreeningpartone",
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
            model_name="historicalscreeningpartone",
            name="fasting_glucose",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=8,
                null=True,
                verbose_name="Fasting glucose <u>level</u>",
            ),
        ),
        migrations.AlterField(
            model_name="historicalscreeningpartone",
            name="fasting_glucose_datetime",
            field=models.DateTimeField(
                blank=True,
                null=True,
                verbose_name="<u>Time</u> fasting glucose <u>level</u> measured",
            ),
        ),
        migrations.AlterField(
            model_name="historicalscreeningpartone",
            name="fasting_glucose_units",
            field=models.CharField(
                blank=True,
                choices=[("mg/dL", "mg/dL"), ("mmol/L", "mmol/L")],
                max_length=15,
                null=True,
                verbose_name="Units (fasting glucose)",
            ),
        ),
        migrations.AlterField(
            model_name="historicalscreeningpartone",
            name="ogtt_base_datetime",
            field=models.DateTimeField(
                blank=True,
                help_text="(glucose solution given)",
                null=True,
                verbose_name="<u>Time</u> oral glucose solution was given",
            ),
        ),
        migrations.AlterField(
            model_name="historicalscreeningpartone",
            name="ogtt_two_hr",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=8,
                null=True,
                verbose_name="Blood glucose <u>level</u> 2-hours after oral glucose solution given",
            ),
        ),
        migrations.AlterField(
            model_name="historicalscreeningpartone",
            name="ogtt_two_hr_datetime",
            field=models.DateTimeField(
                blank=True,
                help_text="(2 hours after glucose solution given)",
                null=True,
                verbose_name="<u>Time</u> blood glucose measured 2-hours after oral glucose solution given",
            ),
        ),
        migrations.AlterField(
            model_name="historicalscreeningpartone",
            name="ogtt_two_hr_units",
            field=models.CharField(
                blank=True,
                choices=[("mg/dL", "mg/dL"), ("mmol/L", "mmol/L")],
                max_length=15,
                null=True,
                verbose_name="Units (Blood glucose 2hrs after...)",
            ),
        ),
        migrations.AlterField(
            model_name="historicalscreeningpartthree",
            name="converted_ogtt_two_hr",
            field=models.DecimalField(
                decimal_places=4,
                help_text="mmol/L (system converted)",
                max_digits=8,
                null=True,
                verbose_name="Blood glucose level 2-hours",
            ),
        ),
        migrations.AlterField(
            model_name="historicalscreeningpartthree",
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
            model_name="historicalscreeningpartthree",
            name="fasting_glucose",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=8,
                null=True,
                verbose_name="Fasting glucose <u>level</u>",
            ),
        ),
        migrations.AlterField(
            model_name="historicalscreeningpartthree",
            name="fasting_glucose_datetime",
            field=models.DateTimeField(
                blank=True,
                null=True,
                verbose_name="<u>Time</u> fasting glucose <u>level</u> measured",
            ),
        ),
        migrations.AlterField(
            model_name="historicalscreeningpartthree",
            name="fasting_glucose_units",
            field=models.CharField(
                blank=True,
                choices=[("mg/dL", "mg/dL"), ("mmol/L", "mmol/L")],
                max_length=15,
                null=True,
                verbose_name="Units (fasting glucose)",
            ),
        ),
        migrations.AlterField(
            model_name="historicalscreeningpartthree",
            name="ogtt_base_datetime",
            field=models.DateTimeField(
                blank=True,
                help_text="(glucose solution given)",
                null=True,
                verbose_name="<u>Time</u> oral glucose solution was given",
            ),
        ),
        migrations.AlterField(
            model_name="historicalscreeningpartthree",
            name="ogtt_two_hr",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=8,
                null=True,
                verbose_name="Blood glucose <u>level</u> 2-hours after oral glucose solution given",
            ),
        ),
        migrations.AlterField(
            model_name="historicalscreeningpartthree",
            name="ogtt_two_hr_datetime",
            field=models.DateTimeField(
                blank=True,
                help_text="(2 hours after glucose solution given)",
                null=True,
                verbose_name="<u>Time</u> blood glucose measured 2-hours after oral glucose solution given",
            ),
        ),
        migrations.AlterField(
            model_name="historicalscreeningpartthree",
            name="ogtt_two_hr_units",
            field=models.CharField(
                blank=True,
                choices=[("mg/dL", "mg/dL"), ("mmol/L", "mmol/L")],
                max_length=15,
                null=True,
                verbose_name="Units (Blood glucose 2hrs after...)",
            ),
        ),
        migrations.AlterField(
            model_name="historicalscreeningparttwo",
            name="converted_ogtt_two_hr",
            field=models.DecimalField(
                decimal_places=4,
                help_text="mmol/L (system converted)",
                max_digits=8,
                null=True,
                verbose_name="Blood glucose level 2-hours",
            ),
        ),
        migrations.AlterField(
            model_name="historicalscreeningparttwo",
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
            model_name="historicalscreeningparttwo",
            name="fasting_glucose",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=8,
                null=True,
                verbose_name="Fasting glucose <u>level</u>",
            ),
        ),
        migrations.AlterField(
            model_name="historicalscreeningparttwo",
            name="fasting_glucose_datetime",
            field=models.DateTimeField(
                blank=True,
                null=True,
                verbose_name="<u>Time</u> fasting glucose <u>level</u> measured",
            ),
        ),
        migrations.AlterField(
            model_name="historicalscreeningparttwo",
            name="fasting_glucose_units",
            field=models.CharField(
                blank=True,
                choices=[("mg/dL", "mg/dL"), ("mmol/L", "mmol/L")],
                max_length=15,
                null=True,
                verbose_name="Units (fasting glucose)",
            ),
        ),
        migrations.AlterField(
            model_name="historicalscreeningparttwo",
            name="ogtt_base_datetime",
            field=models.DateTimeField(
                blank=True,
                help_text="(glucose solution given)",
                null=True,
                verbose_name="<u>Time</u> oral glucose solution was given",
            ),
        ),
        migrations.AlterField(
            model_name="historicalscreeningparttwo",
            name="ogtt_two_hr",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=8,
                null=True,
                verbose_name="Blood glucose <u>level</u> 2-hours after oral glucose solution given",
            ),
        ),
        migrations.AlterField(
            model_name="historicalscreeningparttwo",
            name="ogtt_two_hr_datetime",
            field=models.DateTimeField(
                blank=True,
                help_text="(2 hours after glucose solution given)",
                null=True,
                verbose_name="<u>Time</u> blood glucose measured 2-hours after oral glucose solution given",
            ),
        ),
        migrations.AlterField(
            model_name="historicalscreeningparttwo",
            name="ogtt_two_hr_units",
            field=models.CharField(
                blank=True,
                choices=[("mg/dL", "mg/dL"), ("mmol/L", "mmol/L")],
                max_length=15,
                null=True,
                verbose_name="Units (Blood glucose 2hrs after...)",
            ),
        ),
        migrations.AlterField(
            model_name="historicalsubjectscreening",
            name="converted_ogtt_two_hr",
            field=models.DecimalField(
                decimal_places=4,
                help_text="mmol/L (system converted)",
                max_digits=8,
                null=True,
                verbose_name="Blood glucose level 2-hours",
            ),
        ),
        migrations.AlterField(
            model_name="historicalsubjectscreening",
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
            model_name="historicalsubjectscreening",
            name="fasting_glucose",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=8,
                null=True,
                verbose_name="Fasting glucose <u>level</u>",
            ),
        ),
        migrations.AlterField(
            model_name="historicalsubjectscreening",
            name="fasting_glucose_datetime",
            field=models.DateTimeField(
                blank=True,
                null=True,
                verbose_name="<u>Time</u> fasting glucose <u>level</u> measured",
            ),
        ),
        migrations.AlterField(
            model_name="historicalsubjectscreening",
            name="fasting_glucose_units",
            field=models.CharField(
                blank=True,
                choices=[("mg/dL", "mg/dL"), ("mmol/L", "mmol/L")],
                max_length=15,
                null=True,
                verbose_name="Units (fasting glucose)",
            ),
        ),
        migrations.AlterField(
            model_name="historicalsubjectscreening",
            name="ogtt_base_datetime",
            field=models.DateTimeField(
                blank=True,
                help_text="(glucose solution given)",
                null=True,
                verbose_name="<u>Time</u> oral glucose solution was given",
            ),
        ),
        migrations.AlterField(
            model_name="historicalsubjectscreening",
            name="ogtt_two_hr",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=8,
                null=True,
                verbose_name="Blood glucose <u>level</u> 2-hours after oral glucose solution given",
            ),
        ),
        migrations.AlterField(
            model_name="historicalsubjectscreening",
            name="ogtt_two_hr_datetime",
            field=models.DateTimeField(
                blank=True,
                help_text="(2 hours after glucose solution given)",
                null=True,
                verbose_name="<u>Time</u> blood glucose measured 2-hours after oral glucose solution given",
            ),
        ),
        migrations.AlterField(
            model_name="historicalsubjectscreening",
            name="ogtt_two_hr_units",
            field=models.CharField(
                blank=True,
                choices=[("mg/dL", "mg/dL"), ("mmol/L", "mmol/L")],
                max_length=15,
                null=True,
                verbose_name="Units (Blood glucose 2hrs after...)",
            ),
        ),
        migrations.AlterField(
            model_name="subjectscreening",
            name="converted_ogtt_two_hr",
            field=models.DecimalField(
                decimal_places=4,
                help_text="mmol/L (system converted)",
                max_digits=8,
                null=True,
                verbose_name="Blood glucose level 2-hours",
            ),
        ),
        migrations.AlterField(
            model_name="subjectscreening",
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
            model_name="subjectscreening",
            name="fasting_glucose",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=8,
                null=True,
                verbose_name="Fasting glucose <u>level</u>",
            ),
        ),
        migrations.AlterField(
            model_name="subjectscreening",
            name="fasting_glucose_datetime",
            field=models.DateTimeField(
                blank=True,
                null=True,
                verbose_name="<u>Time</u> fasting glucose <u>level</u> measured",
            ),
        ),
        migrations.AlterField(
            model_name="subjectscreening",
            name="fasting_glucose_units",
            field=models.CharField(
                blank=True,
                choices=[("mg/dL", "mg/dL"), ("mmol/L", "mmol/L")],
                max_length=15,
                null=True,
                verbose_name="Units (fasting glucose)",
            ),
        ),
        migrations.AlterField(
            model_name="subjectscreening",
            name="ogtt_base_datetime",
            field=models.DateTimeField(
                blank=True,
                help_text="(glucose solution given)",
                null=True,
                verbose_name="<u>Time</u> oral glucose solution was given",
            ),
        ),
        migrations.AlterField(
            model_name="subjectscreening",
            name="ogtt_two_hr",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=8,
                null=True,
                verbose_name="Blood glucose <u>level</u> 2-hours after oral glucose solution given",
            ),
        ),
        migrations.AlterField(
            model_name="subjectscreening",
            name="ogtt_two_hr_datetime",
            field=models.DateTimeField(
                blank=True,
                help_text="(2 hours after glucose solution given)",
                null=True,
                verbose_name="<u>Time</u> blood glucose measured 2-hours after oral glucose solution given",
            ),
        ),
        migrations.AlterField(
            model_name="subjectscreening",
            name="ogtt_two_hr_units",
            field=models.CharField(
                blank=True,
                choices=[("mg/dL", "mg/dL"), ("mmol/L", "mmol/L")],
                max_length=15,
                null=True,
                verbose_name="Units (Blood glucose 2hrs after...)",
            ),
        ),
    ]

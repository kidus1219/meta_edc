# Generated by Django 3.2.11 on 2022-03-04 19:33

import django.core.validators
import edc_model.validators.date
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("meta_screening", "0034_auto_20220304_0508"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="historicalscreeningpartone",
            name="ogtt2_performed",
        ),
        migrations.RemoveField(
            model_name="historicalscreeningpartthree",
            name="ogtt2_performed",
        ),
        migrations.RemoveField(
            model_name="historicalscreeningparttwo",
            name="ogtt2_performed",
        ),
        migrations.RemoveField(
            model_name="historicalsubjectscreening",
            name="ogtt2_performed",
        ),
        migrations.RemoveField(
            model_name="subjectscreening",
            name="ogtt2_performed",
        ),
        migrations.AddField(
            model_name="historicalscreeningpartone",
            name="converted_ifg2_value",
            field=models.DecimalField(
                decimal_places=4,
                help_text="mmol/L (system converted)",
                max_digits=8,
                null=True,
                verbose_name="REPEAT Fasting glucose",
            ),
        ),
        migrations.AddField(
            model_name="historicalscreeningpartone",
            name="converted_ogtt2_value",
            field=models.DecimalField(
                decimal_places=4,
                help_text="mmol/L (system converted)",
                max_digits=8,
                null=True,
                verbose_name="REPEAT Blood glucose level 2-hours",
            ),
        ),
        migrations.AddField(
            model_name="historicalscreeningpartone",
            name="ifg2_datetime",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="<u>Time</u> FBG level measured"
            ),
        ),
        migrations.AddField(
            model_name="historicalscreeningpartone",
            name="ifg2_quantifier",
            field=models.CharField(
                choices=[
                    ("=", "="),
                    (">", ">"),
                    (">=", ">="),
                    ("<", "<"),
                    ("<=", "<="),
                ],
                default="=",
                max_length=10,
                verbose_name="FBG quantifier",
            ),
        ),
        migrations.AddField(
            model_name="historicalscreeningpartone",
            name="ifg2_units",
            field=models.CharField(
                blank=True,
                choices=[("mg/dL", "mg/dL"), ("mmol/L", "mmol/L (millimoles/L)")],
                max_length=15,
                null=True,
                verbose_name="IFG units",
            ),
        ),
        migrations.AddField(
            model_name="historicalscreeningpartone",
            name="ifg2_value",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                help_text="A `HIGH` reading may be entered as 9999.99",
                max_digits=8,
                null=True,
                verbose_name="FBG level",
            ),
        ),
        migrations.AddField(
            model_name="historicalscreeningpartone",
            name="repeat_fasting",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No")],
                help_text="As reported by patient",
                max_length=15,
                null=True,
                verbose_name="Has the participant fasted?",
            ),
        ),
        migrations.AddField(
            model_name="historicalscreeningpartone",
            name="repeat_fasting_duration_minutes",
            field=models.IntegerField(help_text="system calculated value", null=True),
        ),
        migrations.AddField(
            model_name="historicalscreeningpartone",
            name="repeat_fasting_duration_str",
            field=models.CharField(
                blank=True,
                help_text="As reported by patient. Duration of fast. Format is `HHhMMm`. For example 1h23m, 12h7m, etc",
                max_length=8,
                null=True,
                validators=[
                    django.core.validators.RegexValidator(
                        "^([0-9]{1,3}h([0-5]?[0-9]m)?)$",
                        message="Invalid format. Expected something like 1h20m, 11h5m, etc",
                    )
                ],
                verbose_name="How long have they fasted in hours and/or minutes?",
            ),
        ),
        migrations.AddField(
            model_name="historicalscreeningpartone",
            name="repeat_fasting_opinion",
            field=models.CharField(
                blank=True,
                choices=[("Yes", "Yes"), ("No", "No"), ("not_sure", "Not sure")],
                max_length=15,
                null=True,
                verbose_name="In the opinion of the clinican, has the participant fasted for these repeat glucose measurement?",
            ),
        ),
        migrations.AddField(
            model_name="historicalscreeningpartone",
            name="repeat_glucose_opinion",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No")],
                default="No",
                help_text="If to be repeated, do so at least 3 days after the first OGTT",
                max_length=15,
                verbose_name="In opinion of the clinician, should the glucose measurements be repeated?",
            ),
        ),
        migrations.AddField(
            model_name="historicalscreeningpartone",
            name="repeat_glucose_performed",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No"), ("PENDING", "Pending")],
                default="No",
                help_text="If repeated, must be at least 3 days after the first glucose measures (FBG, OGTT)",
                max_length=15,
                verbose_name="Were the glucose measurements repeated?",
            ),
        ),
        migrations.AddField(
            model_name="historicalscreeningpartthree",
            name="converted_ifg2_value",
            field=models.DecimalField(
                decimal_places=4,
                help_text="mmol/L (system converted)",
                max_digits=8,
                null=True,
                verbose_name="REPEAT Fasting glucose",
            ),
        ),
        migrations.AddField(
            model_name="historicalscreeningpartthree",
            name="converted_ogtt2_value",
            field=models.DecimalField(
                decimal_places=4,
                help_text="mmol/L (system converted)",
                max_digits=8,
                null=True,
                verbose_name="REPEAT Blood glucose level 2-hours",
            ),
        ),
        migrations.AddField(
            model_name="historicalscreeningpartthree",
            name="ifg2_datetime",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="<u>Time</u> FBG level measured"
            ),
        ),
        migrations.AddField(
            model_name="historicalscreeningpartthree",
            name="ifg2_quantifier",
            field=models.CharField(
                choices=[
                    ("=", "="),
                    (">", ">"),
                    (">=", ">="),
                    ("<", "<"),
                    ("<=", "<="),
                ],
                default="=",
                max_length=10,
                verbose_name="FBG quantifier",
            ),
        ),
        migrations.AddField(
            model_name="historicalscreeningpartthree",
            name="ifg2_units",
            field=models.CharField(
                blank=True,
                choices=[("mg/dL", "mg/dL"), ("mmol/L", "mmol/L (millimoles/L)")],
                max_length=15,
                null=True,
                verbose_name="IFG units",
            ),
        ),
        migrations.AddField(
            model_name="historicalscreeningpartthree",
            name="ifg2_value",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                help_text="A `HIGH` reading may be entered as 9999.99",
                max_digits=8,
                null=True,
                verbose_name="FBG level",
            ),
        ),
        migrations.AddField(
            model_name="historicalscreeningpartthree",
            name="repeat_fasting",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No")],
                help_text="As reported by patient",
                max_length=15,
                null=True,
                verbose_name="Has the participant fasted?",
            ),
        ),
        migrations.AddField(
            model_name="historicalscreeningpartthree",
            name="repeat_fasting_duration_minutes",
            field=models.IntegerField(help_text="system calculated value", null=True),
        ),
        migrations.AddField(
            model_name="historicalscreeningpartthree",
            name="repeat_fasting_duration_str",
            field=models.CharField(
                blank=True,
                help_text="As reported by patient. Duration of fast. Format is `HHhMMm`. For example 1h23m, 12h7m, etc",
                max_length=8,
                null=True,
                validators=[
                    django.core.validators.RegexValidator(
                        "^([0-9]{1,3}h([0-5]?[0-9]m)?)$",
                        message="Invalid format. Expected something like 1h20m, 11h5m, etc",
                    )
                ],
                verbose_name="How long have they fasted in hours and/or minutes?",
            ),
        ),
        migrations.AddField(
            model_name="historicalscreeningpartthree",
            name="repeat_fasting_opinion",
            field=models.CharField(
                blank=True,
                choices=[("Yes", "Yes"), ("No", "No"), ("not_sure", "Not sure")],
                max_length=15,
                null=True,
                verbose_name="In the opinion of the clinican, has the participant fasted for these repeat glucose measurement?",
            ),
        ),
        migrations.AddField(
            model_name="historicalscreeningpartthree",
            name="repeat_glucose_opinion",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No")],
                default="No",
                help_text="If to be repeated, do so at least 3 days after the first OGTT",
                max_length=15,
                verbose_name="In opinion of the clinician, should the glucose measurements be repeated?",
            ),
        ),
        migrations.AddField(
            model_name="historicalscreeningpartthree",
            name="repeat_glucose_performed",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No"), ("PENDING", "Pending")],
                default="No",
                help_text="If repeated, must be at least 3 days after the first glucose measures (FBG, OGTT)",
                max_length=15,
                verbose_name="Were the glucose measurements repeated?",
            ),
        ),
        migrations.AddField(
            model_name="historicalscreeningparttwo",
            name="converted_ifg2_value",
            field=models.DecimalField(
                decimal_places=4,
                help_text="mmol/L (system converted)",
                max_digits=8,
                null=True,
                verbose_name="REPEAT Fasting glucose",
            ),
        ),
        migrations.AddField(
            model_name="historicalscreeningparttwo",
            name="converted_ogtt2_value",
            field=models.DecimalField(
                decimal_places=4,
                help_text="mmol/L (system converted)",
                max_digits=8,
                null=True,
                verbose_name="REPEAT Blood glucose level 2-hours",
            ),
        ),
        migrations.AddField(
            model_name="historicalscreeningparttwo",
            name="ifg2_datetime",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="<u>Time</u> FBG level measured"
            ),
        ),
        migrations.AddField(
            model_name="historicalscreeningparttwo",
            name="ifg2_quantifier",
            field=models.CharField(
                choices=[
                    ("=", "="),
                    (">", ">"),
                    (">=", ">="),
                    ("<", "<"),
                    ("<=", "<="),
                ],
                default="=",
                max_length=10,
                verbose_name="FBG quantifier",
            ),
        ),
        migrations.AddField(
            model_name="historicalscreeningparttwo",
            name="ifg2_units",
            field=models.CharField(
                blank=True,
                choices=[("mg/dL", "mg/dL"), ("mmol/L", "mmol/L (millimoles/L)")],
                max_length=15,
                null=True,
                verbose_name="IFG units",
            ),
        ),
        migrations.AddField(
            model_name="historicalscreeningparttwo",
            name="ifg2_value",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                help_text="A `HIGH` reading may be entered as 9999.99",
                max_digits=8,
                null=True,
                verbose_name="FBG level",
            ),
        ),
        migrations.AddField(
            model_name="historicalscreeningparttwo",
            name="repeat_fasting",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No")],
                help_text="As reported by patient",
                max_length=15,
                null=True,
                verbose_name="Has the participant fasted?",
            ),
        ),
        migrations.AddField(
            model_name="historicalscreeningparttwo",
            name="repeat_fasting_duration_minutes",
            field=models.IntegerField(help_text="system calculated value", null=True),
        ),
        migrations.AddField(
            model_name="historicalscreeningparttwo",
            name="repeat_fasting_duration_str",
            field=models.CharField(
                blank=True,
                help_text="As reported by patient. Duration of fast. Format is `HHhMMm`. For example 1h23m, 12h7m, etc",
                max_length=8,
                null=True,
                validators=[
                    django.core.validators.RegexValidator(
                        "^([0-9]{1,3}h([0-5]?[0-9]m)?)$",
                        message="Invalid format. Expected something like 1h20m, 11h5m, etc",
                    )
                ],
                verbose_name="How long have they fasted in hours and/or minutes?",
            ),
        ),
        migrations.AddField(
            model_name="historicalscreeningparttwo",
            name="repeat_fasting_opinion",
            field=models.CharField(
                blank=True,
                choices=[("Yes", "Yes"), ("No", "No"), ("not_sure", "Not sure")],
                max_length=15,
                null=True,
                verbose_name="In the opinion of the clinican, has the participant fasted for these repeat glucose measurement?",
            ),
        ),
        migrations.AddField(
            model_name="historicalscreeningparttwo",
            name="repeat_glucose_opinion",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No")],
                default="No",
                help_text="If to be repeated, do so at least 3 days after the first OGTT",
                max_length=15,
                verbose_name="In opinion of the clinician, should the glucose measurements be repeated?",
            ),
        ),
        migrations.AddField(
            model_name="historicalscreeningparttwo",
            name="repeat_glucose_performed",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No"), ("PENDING", "Pending")],
                default="No",
                help_text="If repeated, must be at least 3 days after the first glucose measures (FBG, OGTT)",
                max_length=15,
                verbose_name="Were the glucose measurements repeated?",
            ),
        ),
        migrations.AddField(
            model_name="historicalsubjectscreening",
            name="converted_ifg2_value",
            field=models.DecimalField(
                decimal_places=4,
                help_text="mmol/L (system converted)",
                max_digits=8,
                null=True,
                verbose_name="REPEAT Fasting glucose",
            ),
        ),
        migrations.AddField(
            model_name="historicalsubjectscreening",
            name="converted_ogtt2_value",
            field=models.DecimalField(
                decimal_places=4,
                help_text="mmol/L (system converted)",
                max_digits=8,
                null=True,
                verbose_name="REPEAT Blood glucose level 2-hours",
            ),
        ),
        migrations.AddField(
            model_name="historicalsubjectscreening",
            name="ifg2_datetime",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="<u>Time</u> FBG level measured"
            ),
        ),
        migrations.AddField(
            model_name="historicalsubjectscreening",
            name="ifg2_quantifier",
            field=models.CharField(
                choices=[
                    ("=", "="),
                    (">", ">"),
                    (">=", ">="),
                    ("<", "<"),
                    ("<=", "<="),
                ],
                default="=",
                max_length=10,
                verbose_name="FBG quantifier",
            ),
        ),
        migrations.AddField(
            model_name="historicalsubjectscreening",
            name="ifg2_units",
            field=models.CharField(
                blank=True,
                choices=[("mg/dL", "mg/dL"), ("mmol/L", "mmol/L (millimoles/L)")],
                max_length=15,
                null=True,
                verbose_name="IFG units",
            ),
        ),
        migrations.AddField(
            model_name="historicalsubjectscreening",
            name="ifg2_value",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                help_text="A `HIGH` reading may be entered as 9999.99",
                max_digits=8,
                null=True,
                verbose_name="FBG level",
            ),
        ),
        migrations.AddField(
            model_name="historicalsubjectscreening",
            name="repeat_fasting",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No")],
                help_text="As reported by patient",
                max_length=15,
                null=True,
                verbose_name="Has the participant fasted?",
            ),
        ),
        migrations.AddField(
            model_name="historicalsubjectscreening",
            name="repeat_fasting_duration_minutes",
            field=models.IntegerField(help_text="system calculated value", null=True),
        ),
        migrations.AddField(
            model_name="historicalsubjectscreening",
            name="repeat_fasting_duration_str",
            field=models.CharField(
                blank=True,
                help_text="As reported by patient. Duration of fast. Format is `HHhMMm`. For example 1h23m, 12h7m, etc",
                max_length=8,
                null=True,
                validators=[
                    django.core.validators.RegexValidator(
                        "^([0-9]{1,3}h([0-5]?[0-9]m)?)$",
                        message="Invalid format. Expected something like 1h20m, 11h5m, etc",
                    )
                ],
                verbose_name="How long have they fasted in hours and/or minutes?",
            ),
        ),
        migrations.AddField(
            model_name="historicalsubjectscreening",
            name="repeat_fasting_opinion",
            field=models.CharField(
                blank=True,
                choices=[("Yes", "Yes"), ("No", "No"), ("not_sure", "Not sure")],
                max_length=15,
                null=True,
                verbose_name="In the opinion of the clinican, has the participant fasted for these repeat glucose measurement?",
            ),
        ),
        migrations.AddField(
            model_name="historicalsubjectscreening",
            name="repeat_glucose_opinion",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No")],
                default="No",
                help_text="If to be repeated, do so at least 3 days after the first OGTT",
                max_length=15,
                verbose_name="In opinion of the clinician, should the glucose measurements be repeated?",
            ),
        ),
        migrations.AddField(
            model_name="historicalsubjectscreening",
            name="repeat_glucose_performed",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No"), ("PENDING", "Pending")],
                default="No",
                help_text="If repeated, must be at least 3 days after the first glucose measures (FBG, OGTT)",
                max_length=15,
                verbose_name="Were the glucose measurements repeated?",
            ),
        ),
        migrations.AddField(
            model_name="subjectscreening",
            name="converted_ifg2_value",
            field=models.DecimalField(
                decimal_places=4,
                help_text="mmol/L (system converted)",
                max_digits=8,
                null=True,
                verbose_name="REPEAT Fasting glucose",
            ),
        ),
        migrations.AddField(
            model_name="subjectscreening",
            name="converted_ogtt2_value",
            field=models.DecimalField(
                decimal_places=4,
                help_text="mmol/L (system converted)",
                max_digits=8,
                null=True,
                verbose_name="REPEAT Blood glucose level 2-hours",
            ),
        ),
        migrations.AddField(
            model_name="subjectscreening",
            name="ifg2_datetime",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="<u>Time</u> FBG level measured"
            ),
        ),
        migrations.AddField(
            model_name="subjectscreening",
            name="ifg2_quantifier",
            field=models.CharField(
                choices=[
                    ("=", "="),
                    (">", ">"),
                    (">=", ">="),
                    ("<", "<"),
                    ("<=", "<="),
                ],
                default="=",
                max_length=10,
                verbose_name="FBG quantifier",
            ),
        ),
        migrations.AddField(
            model_name="subjectscreening",
            name="ifg2_units",
            field=models.CharField(
                blank=True,
                choices=[("mg/dL", "mg/dL"), ("mmol/L", "mmol/L (millimoles/L)")],
                max_length=15,
                null=True,
                verbose_name="IFG units",
            ),
        ),
        migrations.AddField(
            model_name="subjectscreening",
            name="ifg2_value",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                help_text="A `HIGH` reading may be entered as 9999.99",
                max_digits=8,
                null=True,
                verbose_name="FBG level",
            ),
        ),
        migrations.AddField(
            model_name="subjectscreening",
            name="repeat_fasting",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No")],
                help_text="As reported by patient",
                max_length=15,
                null=True,
                verbose_name="Has the participant fasted?",
            ),
        ),
        migrations.AddField(
            model_name="subjectscreening",
            name="repeat_fasting_duration_minutes",
            field=models.IntegerField(help_text="system calculated value", null=True),
        ),
        migrations.AddField(
            model_name="subjectscreening",
            name="repeat_fasting_duration_str",
            field=models.CharField(
                blank=True,
                help_text="As reported by patient. Duration of fast. Format is `HHhMMm`. For example 1h23m, 12h7m, etc",
                max_length=8,
                null=True,
                validators=[
                    django.core.validators.RegexValidator(
                        "^([0-9]{1,3}h([0-5]?[0-9]m)?)$",
                        message="Invalid format. Expected something like 1h20m, 11h5m, etc",
                    )
                ],
                verbose_name="How long have they fasted in hours and/or minutes?",
            ),
        ),
        migrations.AddField(
            model_name="subjectscreening",
            name="repeat_fasting_opinion",
            field=models.CharField(
                blank=True,
                choices=[("Yes", "Yes"), ("No", "No"), ("not_sure", "Not sure")],
                max_length=15,
                null=True,
                verbose_name="In the opinion of the clinican, has the participant fasted for these repeat glucose measurement?",
            ),
        ),
        migrations.AddField(
            model_name="subjectscreening",
            name="repeat_glucose_opinion",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No")],
                default="No",
                help_text="If to be repeated, do so at least 3 days after the first OGTT",
                max_length=15,
                verbose_name="In opinion of the clinician, should the glucose measurements be repeated?",
            ),
        ),
        migrations.AddField(
            model_name="subjectscreening",
            name="repeat_glucose_performed",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No"), ("PENDING", "Pending")],
                default="No",
                help_text="If repeated, must be at least 3 days after the first glucose measures (FBG, OGTT)",
                max_length=15,
                verbose_name="Were the glucose measurements repeated?",
            ),
        ),
        migrations.AlterField(
            model_name="historicalscreeningpartone",
            name="ogtt2_base_datetime",
            field=models.DateTimeField(
                blank=True,
                help_text="(glucose solution given)",
                null=True,
                validators=[edc_model.validators.date.datetime_not_future],
                verbose_name="<u>Time</u> oral glucose solution was given",
            ),
        ),
        migrations.AlterField(
            model_name="historicalscreeningpartone",
            name="ogtt2_datetime",
            field=models.DateTimeField(
                blank=True,
                help_text="(2 hours after glucose solution given)",
                null=True,
                validators=[edc_model.validators.date.datetime_not_future],
                verbose_name="<u>Time</u> blood glucose measured 2-hours after oral glucose solution given",
            ),
        ),
        migrations.AlterField(
            model_name="historicalscreeningpartone",
            name="ogtt_base_datetime",
            field=models.DateTimeField(
                blank=True,
                help_text="(glucose solution given)",
                null=True,
                validators=[edc_model.validators.date.datetime_not_future],
                verbose_name="<u>Time</u> oral glucose solution was given",
            ),
        ),
        migrations.AlterField(
            model_name="historicalscreeningpartone",
            name="ogtt_datetime",
            field=models.DateTimeField(
                blank=True,
                help_text="(2 hours after glucose solution given)",
                null=True,
                validators=[edc_model.validators.date.datetime_not_future],
                verbose_name="<u>Time</u> blood glucose measured 2-hours after oral glucose solution given",
            ),
        ),
        migrations.AlterField(
            model_name="historicalscreeningpartthree",
            name="ogtt2_base_datetime",
            field=models.DateTimeField(
                blank=True,
                help_text="(glucose solution given)",
                null=True,
                validators=[edc_model.validators.date.datetime_not_future],
                verbose_name="<u>Time</u> oral glucose solution was given",
            ),
        ),
        migrations.AlterField(
            model_name="historicalscreeningpartthree",
            name="ogtt2_datetime",
            field=models.DateTimeField(
                blank=True,
                help_text="(2 hours after glucose solution given)",
                null=True,
                validators=[edc_model.validators.date.datetime_not_future],
                verbose_name="<u>Time</u> blood glucose measured 2-hours after oral glucose solution given",
            ),
        ),
        migrations.AlterField(
            model_name="historicalscreeningpartthree",
            name="ogtt_base_datetime",
            field=models.DateTimeField(
                blank=True,
                help_text="(glucose solution given)",
                null=True,
                validators=[edc_model.validators.date.datetime_not_future],
                verbose_name="<u>Time</u> oral glucose solution was given",
            ),
        ),
        migrations.AlterField(
            model_name="historicalscreeningpartthree",
            name="ogtt_datetime",
            field=models.DateTimeField(
                blank=True,
                help_text="(2 hours after glucose solution given)",
                null=True,
                validators=[edc_model.validators.date.datetime_not_future],
                verbose_name="<u>Time</u> blood glucose measured 2-hours after oral glucose solution given",
            ),
        ),
        migrations.AlterField(
            model_name="historicalscreeningparttwo",
            name="ogtt2_base_datetime",
            field=models.DateTimeField(
                blank=True,
                help_text="(glucose solution given)",
                null=True,
                validators=[edc_model.validators.date.datetime_not_future],
                verbose_name="<u>Time</u> oral glucose solution was given",
            ),
        ),
        migrations.AlterField(
            model_name="historicalscreeningparttwo",
            name="ogtt2_datetime",
            field=models.DateTimeField(
                blank=True,
                help_text="(2 hours after glucose solution given)",
                null=True,
                validators=[edc_model.validators.date.datetime_not_future],
                verbose_name="<u>Time</u> blood glucose measured 2-hours after oral glucose solution given",
            ),
        ),
        migrations.AlterField(
            model_name="historicalscreeningparttwo",
            name="ogtt_base_datetime",
            field=models.DateTimeField(
                blank=True,
                help_text="(glucose solution given)",
                null=True,
                validators=[edc_model.validators.date.datetime_not_future],
                verbose_name="<u>Time</u> oral glucose solution was given",
            ),
        ),
        migrations.AlterField(
            model_name="historicalscreeningparttwo",
            name="ogtt_datetime",
            field=models.DateTimeField(
                blank=True,
                help_text="(2 hours after glucose solution given)",
                null=True,
                validators=[edc_model.validators.date.datetime_not_future],
                verbose_name="<u>Time</u> blood glucose measured 2-hours after oral glucose solution given",
            ),
        ),
        migrations.AlterField(
            model_name="historicalsubjectscreening",
            name="ogtt2_base_datetime",
            field=models.DateTimeField(
                blank=True,
                help_text="(glucose solution given)",
                null=True,
                validators=[edc_model.validators.date.datetime_not_future],
                verbose_name="<u>Time</u> oral glucose solution was given",
            ),
        ),
        migrations.AlterField(
            model_name="historicalsubjectscreening",
            name="ogtt2_datetime",
            field=models.DateTimeField(
                blank=True,
                help_text="(2 hours after glucose solution given)",
                null=True,
                validators=[edc_model.validators.date.datetime_not_future],
                verbose_name="<u>Time</u> blood glucose measured 2-hours after oral glucose solution given",
            ),
        ),
        migrations.AlterField(
            model_name="historicalsubjectscreening",
            name="ogtt_base_datetime",
            field=models.DateTimeField(
                blank=True,
                help_text="(glucose solution given)",
                null=True,
                validators=[edc_model.validators.date.datetime_not_future],
                verbose_name="<u>Time</u> oral glucose solution was given",
            ),
        ),
        migrations.AlterField(
            model_name="historicalsubjectscreening",
            name="ogtt_datetime",
            field=models.DateTimeField(
                blank=True,
                help_text="(2 hours after glucose solution given)",
                null=True,
                validators=[edc_model.validators.date.datetime_not_future],
                verbose_name="<u>Time</u> blood glucose measured 2-hours after oral glucose solution given",
            ),
        ),
        migrations.AlterField(
            model_name="subjectscreening",
            name="ogtt2_base_datetime",
            field=models.DateTimeField(
                blank=True,
                help_text="(glucose solution given)",
                null=True,
                validators=[edc_model.validators.date.datetime_not_future],
                verbose_name="<u>Time</u> oral glucose solution was given",
            ),
        ),
        migrations.AlterField(
            model_name="subjectscreening",
            name="ogtt2_datetime",
            field=models.DateTimeField(
                blank=True,
                help_text="(2 hours after glucose solution given)",
                null=True,
                validators=[edc_model.validators.date.datetime_not_future],
                verbose_name="<u>Time</u> blood glucose measured 2-hours after oral glucose solution given",
            ),
        ),
        migrations.AlterField(
            model_name="subjectscreening",
            name="ogtt_base_datetime",
            field=models.DateTimeField(
                blank=True,
                help_text="(glucose solution given)",
                null=True,
                validators=[edc_model.validators.date.datetime_not_future],
                verbose_name="<u>Time</u> oral glucose solution was given",
            ),
        ),
        migrations.AlterField(
            model_name="subjectscreening",
            name="ogtt_datetime",
            field=models.DateTimeField(
                blank=True,
                help_text="(2 hours after glucose solution given)",
                null=True,
                validators=[edc_model.validators.date.datetime_not_future],
                verbose_name="<u>Time</u> blood glucose measured 2-hours after oral glucose solution given",
            ),
        ),
    ]

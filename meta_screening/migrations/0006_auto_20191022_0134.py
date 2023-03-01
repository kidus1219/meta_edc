# Generated by Django 2.2.6 on 2019-10-21 22:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("meta_screening", "0005_auto_20191021_0353")]

    operations = [
        migrations.AlterField(
            model_name="historicalscreeningpartone",
            name="ogtt_base_datetime",
            field=models.DateTimeField(
                blank=True,
                help_text="(glucose solution given)",
                null=True,
                verbose_name="Time oral glucose solution was given",
            ),
        ),
        migrations.AlterField(
            model_name="historicalscreeningpartone",
            name="ogtt_two_hr",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                help_text="in mmol/L",
                max_digits=8,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(300),
                ],
                verbose_name="Blood glucose level 2-hours after glucose solution given",
            ),
        ),
        migrations.AlterField(
            model_name="historicalscreeningpartone",
            name="ogtt_two_hr_datetime",
            field=models.DateTimeField(
                blank=True,
                null=True,
                verbose_name="Time blood glucose levels 2-hours measured",
            ),
        ),
        migrations.AlterField(
            model_name="historicalscreeningpartthree",
            name="ogtt_base_datetime",
            field=models.DateTimeField(
                blank=True,
                help_text="(glucose solution given)",
                null=True,
                verbose_name="Time oral glucose solution was given",
            ),
        ),
        migrations.AlterField(
            model_name="historicalscreeningpartthree",
            name="ogtt_two_hr",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                help_text="in mmol/L",
                max_digits=8,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(300),
                ],
                verbose_name="Blood glucose level 2-hours after glucose solution given",
            ),
        ),
        migrations.AlterField(
            model_name="historicalscreeningpartthree",
            name="ogtt_two_hr_datetime",
            field=models.DateTimeField(
                blank=True,
                null=True,
                verbose_name="Time blood glucose levels 2-hours measured",
            ),
        ),
        migrations.AlterField(
            model_name="historicalscreeningparttwo",
            name="ogtt_base_datetime",
            field=models.DateTimeField(
                blank=True,
                help_text="(glucose solution given)",
                null=True,
                verbose_name="Time oral glucose solution was given",
            ),
        ),
        migrations.AlterField(
            model_name="historicalscreeningparttwo",
            name="ogtt_two_hr",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                help_text="in mmol/L",
                max_digits=8,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(300),
                ],
                verbose_name="Blood glucose level 2-hours after glucose solution given",
            ),
        ),
        migrations.AlterField(
            model_name="historicalscreeningparttwo",
            name="ogtt_two_hr_datetime",
            field=models.DateTimeField(
                blank=True,
                null=True,
                verbose_name="Time blood glucose levels 2-hours measured",
            ),
        ),
        migrations.AlterField(
            model_name="historicalsubjectscreening",
            name="ogtt_base_datetime",
            field=models.DateTimeField(
                blank=True,
                help_text="(glucose solution given)",
                null=True,
                verbose_name="Time oral glucose solution was given",
            ),
        ),
        migrations.AlterField(
            model_name="historicalsubjectscreening",
            name="ogtt_two_hr",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                help_text="in mmol/L",
                max_digits=8,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(300),
                ],
                verbose_name="Blood glucose level 2-hours after glucose solution given",
            ),
        ),
        migrations.AlterField(
            model_name="historicalsubjectscreening",
            name="ogtt_two_hr_datetime",
            field=models.DateTimeField(
                blank=True,
                null=True,
                verbose_name="Time blood glucose levels 2-hours measured",
            ),
        ),
        migrations.AlterField(
            model_name="subjectscreening",
            name="ogtt_base_datetime",
            field=models.DateTimeField(
                blank=True,
                help_text="(glucose solution given)",
                null=True,
                verbose_name="Time oral glucose solution was given",
            ),
        ),
        migrations.AlterField(
            model_name="subjectscreening",
            name="ogtt_two_hr",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                help_text="in mmol/L",
                max_digits=8,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(300),
                ],
                verbose_name="Blood glucose level 2-hours after glucose solution given",
            ),
        ),
        migrations.AlterField(
            model_name="subjectscreening",
            name="ogtt_two_hr_datetime",
            field=models.DateTimeField(
                blank=True,
                null=True,
                verbose_name="Time blood glucose levels 2-hours measured",
            ),
        ),
    ]

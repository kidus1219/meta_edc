# Generated by Django 3.0.4 on 2020-04-20 11:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("meta_subject", "0024_auto_20200419_2331"),
    ]

    operations = [
        migrations.AddField(
            model_name="coronakap",
            name="diabetic_on_meds",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No"), ("unknown", "Unknown")],
                default=1,
                max_length=25,
                verbose_name="Are you taking medications to control your <u>diabetes</u>?",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="coronakap",
            name="diabetic_year",
            field=models.IntegerField(
                default=1955,
                validators=[
                    django.core.validators.MinValueValidator(1950),
                    django.core.validators.MinValueValidator(2021),
                ],
                verbose_name="What year did you first learn you had <u>diabetes</u>?",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="coronakap",
            name="hiv_pos_year",
            field=models.IntegerField(
                default=1955,
                validators=[
                    django.core.validators.MinValueValidator(1950),
                    django.core.validators.MinValueValidator(2021),
                ],
                verbose_name="What year did you first test positive?",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="coronakap",
            name="hypertensive_on_meds",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No"), ("unknown", "Unknown")],
                default="Yes",
                max_length=25,
                verbose_name="Are you taking medications to control your <u>hypertension</u>?",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="coronakap",
            name="hypertensive_year",
            field=models.IntegerField(
                default=1955,
                validators=[
                    django.core.validators.MinValueValidator(1950),
                    django.core.validators.MinValueValidator(2021),
                ],
                verbose_name="What year did you first learn you had <u>hypertension</u>?",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="historicalcoronakap",
            name="diabetic_on_meds",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No"), ("unknown", "Unknown")],
                default="Yes",
                max_length=25,
                verbose_name="Are you taking medications to control your <u>diabetes</u>?",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="historicalcoronakap",
            name="diabetic_year",
            field=models.IntegerField(
                default=1955,
                validators=[
                    django.core.validators.MinValueValidator(1950),
                    django.core.validators.MinValueValidator(2021),
                ],
                verbose_name="What year did you first learn you had <u>diabetes</u>?",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="historicalcoronakap",
            name="hiv_pos_year",
            field=models.IntegerField(
                default=1955,
                validators=[
                    django.core.validators.MinValueValidator(1950),
                    django.core.validators.MinValueValidator(2021),
                ],
                verbose_name="What year did you first test positive?",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="historicalcoronakap",
            name="hypertensive_on_meds",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No"), ("unknown", "Unknown")],
                default="Yes",
                max_length=25,
                verbose_name="Are you taking medications to control your <u>hypertension</u>?",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="historicalcoronakap",
            name="hypertensive_year",
            field=models.IntegerField(
                default=1955,
                validators=[
                    django.core.validators.MinValueValidator(1950),
                    django.core.validators.MinValueValidator(2021),
                ],
                verbose_name="What year did you first learn you had <u>hypertension</u>?",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="coronakap",
            name="diabetic",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No"), ("unknown", "Unknown")],
                max_length=25,
                verbose_name="Have you been diagnosed with <u>diabetes</u>?",
            ),
        ),
        migrations.AlterField(
            model_name="coronakap",
            name="hypertensive",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No"), ("unknown", "Unknown")],
                max_length=25,
                verbose_name="Have you been diagnosed with <u>hypertension</u>?",
            ),
        ),
        migrations.AlterField(
            model_name="coronakap",
            name="months_on_art",
            field=models.IntegerField(
                blank=True,
                help_text="in months",
                null=True,
                validators=[django.core.validators.MinValueValidator(0)],
                verbose_name="If yes, for how many months you been on antiretroviral therapy?",
            ),
        ),
        migrations.AlterField(
            model_name="historicalcoronakap",
            name="diabetic",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No"), ("unknown", "Unknown")],
                max_length=25,
                verbose_name="Have you been diagnosed with <u>diabetes</u>?",
            ),
        ),
        migrations.AlterField(
            model_name="historicalcoronakap",
            name="hypertensive",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No"), ("unknown", "Unknown")],
                max_length=25,
                verbose_name="Have you been diagnosed with <u>hypertension</u>?",
            ),
        ),
        migrations.AlterField(
            model_name="historicalcoronakap",
            name="months_on_art",
            field=models.IntegerField(
                blank=True,
                help_text="in months",
                null=True,
                validators=[django.core.validators.MinValueValidator(0)],
                verbose_name="If yes, for how many months you been on antiretroviral therapy?",
            ),
        ),
    ]

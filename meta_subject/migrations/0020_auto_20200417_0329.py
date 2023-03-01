# Generated by Django 3.0.4 on 2020-04-17 00:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("meta_subject", "0019_auto_20200417_0315"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="coronakap",
            name="dm_aware",
        ),
        migrations.RemoveField(
            model_name="coronakap",
            name="months_on_art",
        ),
        migrations.RemoveField(
            model_name="historicalcoronakap",
            name="dm_aware",
        ),
        migrations.RemoveField(
            model_name="historicalcoronakap",
            name="months_on_art",
        ),
        migrations.AlterField(
            model_name="coronakap",
            name="employment",
            field=models.CharField(
                choices=[
                    ("professional", "Professional (e.g. office"),
                    ("labourer", "Labourer"),
                    ("housewife_retired", "Housewife, Retired"),
                    ("self_employed", "Small business, self-employed"),
                    ("OTHER", "Other, specify below"),
                ],
                max_length=25,
                verbose_name="Employment",
            ),
        ),
        migrations.AlterField(
            model_name="coronakap",
            name="employment_status",
            field=models.CharField(
                choices=[
                    ("working_for_pay", "Working for pay"),
                    ("unemployed", "Unemployed"),
                    (
                        "not_working_for_pay",
                        "Not working for pay (housewife, retired...)",
                    ),
                ],
                max_length=25,
                verbose_name="Are you employed",
            ),
        ),
        migrations.AlterField(
            model_name="coronakap",
            name="family_infection_likelihood",
            field=models.CharField(
                choices=[
                    ("very", "Very likely"),
                    ("somewhat", "Somewhat likely"),
                    ("unlikely", "Not very likely, unlikely"),
                    ("not_at_all", "Not at all"),
                ],
                max_length=25,
                verbose_name="How likely do you think it is that you or someone in your family will get sick from the coronavirus",
            ),
        ),
        migrations.AlterField(
            model_name="coronakap",
            name="married",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No")],
                max_length=25,
                verbose_name="Are you currently married?",
            ),
        ),
        migrations.AlterField(
            model_name="coronakap",
            name="perceived_threat",
            field=models.IntegerField(
                help_text="On a scale from 1-10",
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(10),
                ],
                verbose_name="On a scale from 1-10, how serious of a public health threat is coronavirus",
            ),
        ),
        migrations.AlterField(
            model_name="coronakap",
            name="personal_infection_likelihood",
            field=models.CharField(
                choices=[
                    ("very", "Very likely"),
                    ("somewhat", "Somewhat likely"),
                    ("unlikely", "Not very likely, unlikely"),
                    ("not_at_all", "Not at all"),
                ],
                max_length=25,
                verbose_name="How likely do you think it is that you will get corona virus",
            ),
        ),
        migrations.AlterField(
            model_name="historicalcoronakap",
            name="employment",
            field=models.CharField(
                choices=[
                    ("professional", "Professional (e.g. office"),
                    ("labourer", "Labourer"),
                    ("housewife_retired", "Housewife, Retired"),
                    ("self_employed", "Small business, self-employed"),
                    ("OTHER", "Other, specify below"),
                ],
                max_length=25,
                verbose_name="Employment",
            ),
        ),
        migrations.AlterField(
            model_name="historicalcoronakap",
            name="employment_status",
            field=models.CharField(
                choices=[
                    ("working_for_pay", "Working for pay"),
                    ("unemployed", "Unemployed"),
                    (
                        "not_working_for_pay",
                        "Not working for pay (housewife, retired...)",
                    ),
                ],
                max_length=25,
                verbose_name="Are you employed",
            ),
        ),
        migrations.AlterField(
            model_name="historicalcoronakap",
            name="family_infection_likelihood",
            field=models.CharField(
                choices=[
                    ("very", "Very likely"),
                    ("somewhat", "Somewhat likely"),
                    ("unlikely", "Not very likely, unlikely"),
                    ("not_at_all", "Not at all"),
                ],
                max_length=25,
                verbose_name="How likely do you think it is that you or someone in your family will get sick from the coronavirus",
            ),
        ),
        migrations.AlterField(
            model_name="historicalcoronakap",
            name="married",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No")],
                max_length=25,
                verbose_name="Are you currently married?",
            ),
        ),
        migrations.AlterField(
            model_name="historicalcoronakap",
            name="perceived_threat",
            field=models.IntegerField(
                help_text="On a scale from 1-10",
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(10),
                ],
                verbose_name="On a scale from 1-10, how serious of a public health threat is coronavirus",
            ),
        ),
        migrations.AlterField(
            model_name="historicalcoronakap",
            name="personal_infection_likelihood",
            field=models.CharField(
                choices=[
                    ("very", "Very likely"),
                    ("somewhat", "Somewhat likely"),
                    ("unlikely", "Not very likely, unlikely"),
                    ("not_at_all", "Not at all"),
                ],
                max_length=25,
                verbose_name="How likely do you think it is that you will get corona virus",
            ),
        ),
    ]

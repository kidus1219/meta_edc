# Generated by Django 3.2.6 on 2021-09-23 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("meta_subject", "0088_auto_20210924_0027"),
    ]

    operations = [
        migrations.AlterField(
            model_name="eq5d3l",
            name="anxiety_depression",
            field=models.CharField(
                choices=[
                    ("not_anxious_depressed", "I am not anxious or depressed"),
                    (
                        "moderately_anxious_depressed",
                        "I am moderately anxious or depressed",
                    ),
                    (
                        "extremely_anxious_depressed",
                        "I am extremely anxious or depressed",
                    ),
                ],
                max_length=45,
                verbose_name="Anxiety / Depression",
            ),
        ),
        migrations.AlterField(
            model_name="eq5d3l",
            name="health_today_score_slider",
            field=models.CharField(
                max_length=3, verbose_name="Visual score for how your health is TODAY"
            ),
        ),
        migrations.AlterField(
            model_name="eq5d3l",
            name="pain_discomfort",
            field=models.CharField(
                choices=[
                    ("no_pain_discomfort", "I have no pain or discomfort"),
                    ("moderate_pain_discomfort", "I have moderate pain or discomfort"),
                    ("extreme_pain_discomfort", "I have extreme pain or discomfort"),
                ],
                max_length=45,
                verbose_name="Pain / Discomfort",
            ),
        ),
        migrations.AlterField(
            model_name="eq5d3l",
            name="self_care",
            field=models.CharField(
                choices=[
                    ("no_problems_with_self_care", "I have no problems with self-care"),
                    (
                        "problems_washing_dressing_myself",
                        "I have some problems washing or dressing myself",
                    ),
                    (
                        "unable_to_wash_dress_myself",
                        "I am unable to wash or dress myself",
                    ),
                ],
                max_length=45,
                verbose_name="Self-care",
            ),
        ),
        migrations.AlterField(
            model_name="eq5d3l",
            name="usual_activities",
            field=models.CharField(
                choices=[
                    (
                        "no_problems_performing_usual_activities",
                        "I have no problems with performing my usual activities",
                    ),
                    (
                        "some_problems_performing_usual_activities",
                        "I have some problems with performing my usual activities",
                    ),
                    (
                        "unable_to_perform_usual_activities",
                        "I am unable to perform my usual activities",
                    ),
                ],
                help_text="Example. work, study, housework, family or leisure activities",
                max_length=45,
                verbose_name="Usual activities",
            ),
        ),
        migrations.AlterField(
            model_name="historicaleq5d3l",
            name="anxiety_depression",
            field=models.CharField(
                choices=[
                    ("not_anxious_depressed", "I am not anxious or depressed"),
                    (
                        "moderately_anxious_depressed",
                        "I am moderately anxious or depressed",
                    ),
                    (
                        "extremely_anxious_depressed",
                        "I am extremely anxious or depressed",
                    ),
                ],
                max_length=45,
                verbose_name="Anxiety / Depression",
            ),
        ),
        migrations.AlterField(
            model_name="historicaleq5d3l",
            name="health_today_score_slider",
            field=models.CharField(
                max_length=3, verbose_name="Visual score for how your health is TODAY"
            ),
        ),
        migrations.AlterField(
            model_name="historicaleq5d3l",
            name="pain_discomfort",
            field=models.CharField(
                choices=[
                    ("no_pain_discomfort", "I have no pain or discomfort"),
                    ("moderate_pain_discomfort", "I have moderate pain or discomfort"),
                    ("extreme_pain_discomfort", "I have extreme pain or discomfort"),
                ],
                max_length=45,
                verbose_name="Pain / Discomfort",
            ),
        ),
        migrations.AlterField(
            model_name="historicaleq5d3l",
            name="self_care",
            field=models.CharField(
                choices=[
                    ("no_problems_with_self_care", "I have no problems with self-care"),
                    (
                        "problems_washing_dressing_myself",
                        "I have some problems washing or dressing myself",
                    ),
                    (
                        "unable_to_wash_dress_myself",
                        "I am unable to wash or dress myself",
                    ),
                ],
                max_length=45,
                verbose_name="Self-care",
            ),
        ),
        migrations.AlterField(
            model_name="historicaleq5d3l",
            name="usual_activities",
            field=models.CharField(
                choices=[
                    (
                        "no_problems_performing_usual_activities",
                        "I have no problems with performing my usual activities",
                    ),
                    (
                        "some_problems_performing_usual_activities",
                        "I have some problems with performing my usual activities",
                    ),
                    (
                        "unable_to_perform_usual_activities",
                        "I am unable to perform my usual activities",
                    ),
                ],
                help_text="Example. work, study, housework, family or leisure activities",
                max_length=45,
                verbose_name="Usual activities",
            ),
        ),
    ]

# Generated by Django 2.2.7 on 2019-11-19 20:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("meta_subject", "0008_auto_20191115_0132"),
    ]

    operations = [
        migrations.AddField(
            model_name="bloodresultsglu",
            name="glucose_quantifier",
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
            ),
        ),
        migrations.AddField(
            model_name="historicalbloodresultsglu",
            name="glucose_quantifier",
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
            ),
        ),
    ]

# Generated by Django 4.0.7 on 2022-08-23 13:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("meta_subject", "0139_alter_bloodresultsins_ins_units_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bloodresultsfbc",
            name="action_identifier",
            field=models.CharField(blank=True, max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name="bloodresultsglu",
            name="action_identifier",
            field=models.CharField(blank=True, max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name="bloodresultshba1c",
            name="action_identifier",
            field=models.CharField(blank=True, max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name="bloodresultsins",
            name="action_identifier",
            field=models.CharField(blank=True, max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name="bloodresultslft",
            name="action_identifier",
            field=models.CharField(blank=True, max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name="bloodresultslipid",
            name="action_identifier",
            field=models.CharField(blank=True, max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name="bloodresultsrft",
            name="action_identifier",
            field=models.CharField(blank=True, max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name="delivery",
            name="action_identifier",
            field=models.CharField(blank=True, max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name="egfrdropnotification",
            name="action_identifier",
            field=models.CharField(blank=True, max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name="historicalbloodresultsfbc",
            name="action_identifier",
            field=models.CharField(blank=True, db_index=True, max_length=50),
        ),
        migrations.AlterField(
            model_name="historicalbloodresultsglu",
            name="action_identifier",
            field=models.CharField(blank=True, db_index=True, max_length=50),
        ),
        migrations.AlterField(
            model_name="historicalbloodresultshba1c",
            name="action_identifier",
            field=models.CharField(blank=True, db_index=True, max_length=50),
        ),
        migrations.AlterField(
            model_name="historicalbloodresultsins",
            name="action_identifier",
            field=models.CharField(blank=True, db_index=True, max_length=50),
        ),
        migrations.AlterField(
            model_name="historicalbloodresultslft",
            name="action_identifier",
            field=models.CharField(blank=True, db_index=True, max_length=50),
        ),
        migrations.AlterField(
            model_name="historicalbloodresultslipid",
            name="action_identifier",
            field=models.CharField(blank=True, db_index=True, max_length=50),
        ),
        migrations.AlterField(
            model_name="historicalbloodresultsrft",
            name="action_identifier",
            field=models.CharField(blank=True, db_index=True, max_length=50),
        ),
        migrations.AlterField(
            model_name="historicaldelivery",
            name="action_identifier",
            field=models.CharField(blank=True, db_index=True, max_length=50),
        ),
        migrations.AlterField(
            model_name="historicalegfrdropnotification",
            name="action_identifier",
            field=models.CharField(blank=True, db_index=True, max_length=50),
        ),
        migrations.AlterField(
            model_name="historicalurinepregnancy",
            name="action_identifier",
            field=models.CharField(blank=True, db_index=True, max_length=50),
        ),
        migrations.AlterField(
            model_name="urinepregnancy",
            name="action_identifier",
            field=models.CharField(blank=True, max_length=50, unique=True),
        ),
    ]

# Generated by Django 3.2.4 on 2021-07-02 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("meta_subject", "0055_auto_20210628_2331"),
    ]

    operations = [
        migrations.RenameField(
            model_name="bloodresultsglu",
            old_name="gluc_abnormal",
            new_name="glucose_abnormal",
        ),
        migrations.RenameField(
            model_name="bloodresultsglu",
            old_name="gluc_quantifier",
            new_name="glucose_quantifier",
        ),
        migrations.RenameField(
            model_name="bloodresultsglu",
            old_name="gluc_reportable",
            new_name="glucose_reportable",
        ),
        migrations.RenameField(
            model_name="bloodresultsglu",
            old_name="gluc_units",
            new_name="glucose_units",
        ),
        migrations.RenameField(
            model_name="historicalbloodresultsglu",
            old_name="gluc_abnormal",
            new_name="glucose_abnormal",
        ),
        migrations.RenameField(
            model_name="historicalbloodresultsglu",
            old_name="gluc_quantifier",
            new_name="glucose_quantifier",
        ),
        migrations.RenameField(
            model_name="historicalbloodresultsglu",
            old_name="gluc_reportable",
            new_name="glucose_reportable",
        ),
        migrations.RenameField(
            model_name="historicalbloodresultsglu",
            old_name="gluc_units",
            new_name="glucose_units",
        ),
        migrations.RenameField(
            model_name="bloodresultsglu",
            old_name="gluc_value",
            new_name="glucose_value",
        ),
        migrations.RenameField(
            model_name="historicalbloodresultsglu",
            old_name="gluc_value",
            new_name="glucose_value",
        ),
        migrations.AlterField(
            model_name="glucose",
            name="ifg_value",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                help_text="A `HIGH` reading may be entered as 9999.99",
                max_digits=8,
                null=True,
                verbose_name="IFG level",
            ),
        ),
        migrations.AlterField(
            model_name="historicalglucose",
            name="ifg_value",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                help_text="A `HIGH` reading may be entered as 9999.99",
                max_digits=8,
                null=True,
                verbose_name="IFG level",
            ),
        ),
        migrations.AlterField(
            model_name="bloodresultsglu",
            name="glucose_value",
            field=models.DecimalField(
                blank=True,
                decimal_places=4,
                help_text="A `HIGH` reading may be entered as 9999.99",
                max_digits=8,
                null=True,
                verbose_name="Blood Glucose",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbloodresultsglu",
            name="glucose_value",
            field=models.DecimalField(
                blank=True,
                decimal_places=4,
                help_text="A `HIGH` reading may be entered as 9999.99",
                max_digits=8,
                null=True,
                verbose_name="Blood Glucose",
            ),
        ),
    ]

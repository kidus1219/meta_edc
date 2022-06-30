# Generated by Django 4.0.5 on 2022-06-29 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meta_subject', '0113_bloodresultsrft_egfr_percent_change_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloodresultsrft',
            name='egfr_percent_change',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True, verbose_name='Percent change from baseline'),
        ),
        migrations.AlterField(
            model_name='historicalbloodresultsrft',
            name='egfr_percent_change',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True, verbose_name='Percent change from baseline'),
        ),
    ]
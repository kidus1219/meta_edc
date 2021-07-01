# Generated by Django 3.2.4 on 2021-06-28 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meta_subject', '0054_auto_20210628_2314'),
    ]

    operations = [
        migrations.AddField(
            model_name='bloodresultsrft',
            name='egfr_abnormal',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=25, null=True, verbose_name='abnormal'),
        ),
        migrations.AddField(
            model_name='bloodresultsrft',
            name='egfr_reportable',
            field=models.CharField(blank=True, choices=[('N/A', 'Not applicable'), ('3', 'Yes, grade 3'), ('4', 'Yes, grade 4'), ('No', 'Not reportable'), ('Already reported', 'Already reported'), ('present_at_baseline', 'Present at baseline')], max_length=25, null=True, verbose_name='reportable'),
        ),
        migrations.AddField(
            model_name='bloodresultsrft',
            name='egfr_units',
            field=models.CharField(blank=True, default='mL/min/1.73 m2', max_length=15, null=True, verbose_name='units'),
        ),
        migrations.AddField(
            model_name='historicalbloodresultsrft',
            name='egfr_abnormal',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=25, null=True, verbose_name='abnormal'),
        ),
        migrations.AddField(
            model_name='historicalbloodresultsrft',
            name='egfr_reportable',
            field=models.CharField(blank=True, choices=[('N/A', 'Not applicable'), ('3', 'Yes, grade 3'), ('4', 'Yes, grade 4'), ('No', 'Not reportable'), ('Already reported', 'Already reported'), ('present_at_baseline', 'Present at baseline')], max_length=25, null=True, verbose_name='reportable'),
        ),
        migrations.AddField(
            model_name='historicalbloodresultsrft',
            name='egfr_units',
            field=models.CharField(blank=True, default='mL/min/1.73 m2', max_length=15, null=True, verbose_name='units'),
        ),
    ]

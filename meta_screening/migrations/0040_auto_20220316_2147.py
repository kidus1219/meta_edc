# Generated by Django 3.2.11 on 2022-03-16 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meta_screening', '0039_auto_20220312_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalscreeningpartone',
            name='converted_fbg2_value',
            field=models.DecimalField(decimal_places=4, help_text='mmol/L (system converted)', max_digits=8, null=True, verbose_name='Repeat FBG level'),
        ),
        migrations.AlterField(
            model_name='historicalscreeningpartone',
            name='converted_ogtt2_value',
            field=models.DecimalField(decimal_places=4, help_text='mmol/L (system converted)', max_digits=8, null=True, verbose_name='Repeat OGTT (2-hours)'),
        ),
        migrations.AlterField(
            model_name='historicalscreeningpartone',
            name='converted_ogtt_value',
            field=models.DecimalField(decimal_places=4, help_text='mmol/L (system converted)', max_digits=8, null=True, verbose_name='OGTT (2-hours)'),
        ),
        migrations.AlterField(
            model_name='historicalscreeningpartone',
            name='fbg_units',
            field=models.CharField(blank=True, choices=[('mg/dL', 'mg/dL'), ('mmol/L', 'mmol/L (millimoles/L)')], max_length=15, null=True, verbose_name='FBG units'),
        ),
        migrations.AlterField(
            model_name='historicalscreeningpartone',
            name='inclusion_a',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('tbd', 'To be determined')], default='tbd', help_text='system calculated', max_length=15, verbose_name='BMI>30 combined with FBG (6.1 to 6.9 mmol/L)'),
        ),
        migrations.AlterField(
            model_name='historicalscreeningpartone',
            name='inclusion_b',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('tbd', 'To be determined')], default='tbd', help_text='system calculated', max_length=15, verbose_name='BMI>30 combined with OGTT (2 hours) (7.0 to 11.10 mmol/L)'),
        ),
        migrations.AlterField(
            model_name='historicalscreeningpartone',
            name='inclusion_c',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('tbd', 'To be determined')], default='tbd', help_text='system calculated', max_length=15, verbose_name='BMI<=30 combined with FBG (6.3 to 6.9 mmol/L)'),
        ),
        migrations.AlterField(
            model_name='historicalscreeningpartone',
            name='inclusion_d',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('tbd', 'To be determined')], default='tbd', help_text='system calculated', max_length=15, verbose_name='BMI<=30 combined with OGTT (2 hours) (9.0 to 11.10 mmol/L)'),
        ),
        migrations.AlterField(
            model_name='historicalscreeningpartone',
            name='ogtt2_units',
            field=models.CharField(blank=True, choices=[('mg/dL', 'mg/dL'), ('mmol/L', 'mmol/L (millimoles/L)')], max_length=15, null=True, verbose_name='Repeat OGTT Units'),
        ),
        migrations.AlterField(
            model_name='historicalscreeningpartone',
            name='ogtt_units',
            field=models.CharField(blank=True, choices=[('mg/dL', 'mg/dL'), ('mmol/L', 'mmol/L (millimoles/L)')], max_length=15, null=True, verbose_name='OGTT Units'),
        ),
        migrations.AlterField(
            model_name='historicalscreeningpartthree',
            name='converted_fbg2_value',
            field=models.DecimalField(decimal_places=4, help_text='mmol/L (system converted)', max_digits=8, null=True, verbose_name='Repeat FBG level'),
        ),
        migrations.AlterField(
            model_name='historicalscreeningpartthree',
            name='converted_ogtt2_value',
            field=models.DecimalField(decimal_places=4, help_text='mmol/L (system converted)', max_digits=8, null=True, verbose_name='Repeat OGTT (2-hours)'),
        ),
        migrations.AlterField(
            model_name='historicalscreeningpartthree',
            name='converted_ogtt_value',
            field=models.DecimalField(decimal_places=4, help_text='mmol/L (system converted)', max_digits=8, null=True, verbose_name='OGTT (2-hours)'),
        ),
        migrations.AlterField(
            model_name='historicalscreeningpartthree',
            name='fbg_units',
            field=models.CharField(blank=True, choices=[('mg/dL', 'mg/dL'), ('mmol/L', 'mmol/L (millimoles/L)')], max_length=15, null=True, verbose_name='FBG units'),
        ),
        migrations.AlterField(
            model_name='historicalscreeningpartthree',
            name='inclusion_a',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('tbd', 'To be determined')], default='tbd', help_text='system calculated', max_length=15, verbose_name='BMI>30 combined with FBG (6.1 to 6.9 mmol/L)'),
        ),
        migrations.AlterField(
            model_name='historicalscreeningpartthree',
            name='inclusion_b',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('tbd', 'To be determined')], default='tbd', help_text='system calculated', max_length=15, verbose_name='BMI>30 combined with OGTT (2 hours) (7.0 to 11.10 mmol/L)'),
        ),
        migrations.AlterField(
            model_name='historicalscreeningpartthree',
            name='inclusion_c',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('tbd', 'To be determined')], default='tbd', help_text='system calculated', max_length=15, verbose_name='BMI<=30 combined with FBG (6.3 to 6.9 mmol/L)'),
        ),
        migrations.AlterField(
            model_name='historicalscreeningpartthree',
            name='inclusion_d',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('tbd', 'To be determined')], default='tbd', help_text='system calculated', max_length=15, verbose_name='BMI<=30 combined with OGTT (2 hours) (9.0 to 11.10 mmol/L)'),
        ),
        migrations.AlterField(
            model_name='historicalscreeningpartthree',
            name='ogtt2_units',
            field=models.CharField(blank=True, choices=[('mg/dL', 'mg/dL'), ('mmol/L', 'mmol/L (millimoles/L)')], max_length=15, null=True, verbose_name='Repeat OGTT Units'),
        ),
        migrations.AlterField(
            model_name='historicalscreeningpartthree',
            name='ogtt_units',
            field=models.CharField(blank=True, choices=[('mg/dL', 'mg/dL'), ('mmol/L', 'mmol/L (millimoles/L)')], max_length=15, null=True, verbose_name='OGTT Units'),
        ),
        migrations.AlterField(
            model_name='historicalscreeningparttwo',
            name='converted_fbg2_value',
            field=models.DecimalField(decimal_places=4, help_text='mmol/L (system converted)', max_digits=8, null=True, verbose_name='Repeat FBG level'),
        ),
        migrations.AlterField(
            model_name='historicalscreeningparttwo',
            name='converted_ogtt2_value',
            field=models.DecimalField(decimal_places=4, help_text='mmol/L (system converted)', max_digits=8, null=True, verbose_name='Repeat OGTT (2-hours)'),
        ),
        migrations.AlterField(
            model_name='historicalscreeningparttwo',
            name='converted_ogtt_value',
            field=models.DecimalField(decimal_places=4, help_text='mmol/L (system converted)', max_digits=8, null=True, verbose_name='OGTT (2-hours)'),
        ),
        migrations.AlterField(
            model_name='historicalscreeningparttwo',
            name='fbg_units',
            field=models.CharField(blank=True, choices=[('mg/dL', 'mg/dL'), ('mmol/L', 'mmol/L (millimoles/L)')], max_length=15, null=True, verbose_name='FBG units'),
        ),
        migrations.AlterField(
            model_name='historicalscreeningparttwo',
            name='inclusion_a',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('tbd', 'To be determined')], default='tbd', help_text='system calculated', max_length=15, verbose_name='BMI>30 combined with FBG (6.1 to 6.9 mmol/L)'),
        ),
        migrations.AlterField(
            model_name='historicalscreeningparttwo',
            name='inclusion_b',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('tbd', 'To be determined')], default='tbd', help_text='system calculated', max_length=15, verbose_name='BMI>30 combined with OGTT (2 hours) (7.0 to 11.10 mmol/L)'),
        ),
        migrations.AlterField(
            model_name='historicalscreeningparttwo',
            name='inclusion_c',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('tbd', 'To be determined')], default='tbd', help_text='system calculated', max_length=15, verbose_name='BMI<=30 combined with FBG (6.3 to 6.9 mmol/L)'),
        ),
        migrations.AlterField(
            model_name='historicalscreeningparttwo',
            name='inclusion_d',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('tbd', 'To be determined')], default='tbd', help_text='system calculated', max_length=15, verbose_name='BMI<=30 combined with OGTT (2 hours) (9.0 to 11.10 mmol/L)'),
        ),
        migrations.AlterField(
            model_name='historicalscreeningparttwo',
            name='ogtt2_units',
            field=models.CharField(blank=True, choices=[('mg/dL', 'mg/dL'), ('mmol/L', 'mmol/L (millimoles/L)')], max_length=15, null=True, verbose_name='Repeat OGTT Units'),
        ),
        migrations.AlterField(
            model_name='historicalscreeningparttwo',
            name='ogtt_units',
            field=models.CharField(blank=True, choices=[('mg/dL', 'mg/dL'), ('mmol/L', 'mmol/L (millimoles/L)')], max_length=15, null=True, verbose_name='OGTT Units'),
        ),
        migrations.AlterField(
            model_name='historicalsubjectscreening',
            name='converted_fbg2_value',
            field=models.DecimalField(decimal_places=4, help_text='mmol/L (system converted)', max_digits=8, null=True, verbose_name='Repeat FBG level'),
        ),
        migrations.AlterField(
            model_name='historicalsubjectscreening',
            name='converted_ogtt2_value',
            field=models.DecimalField(decimal_places=4, help_text='mmol/L (system converted)', max_digits=8, null=True, verbose_name='Repeat OGTT (2-hours)'),
        ),
        migrations.AlterField(
            model_name='historicalsubjectscreening',
            name='converted_ogtt_value',
            field=models.DecimalField(decimal_places=4, help_text='mmol/L (system converted)', max_digits=8, null=True, verbose_name='OGTT (2-hours)'),
        ),
        migrations.AlterField(
            model_name='historicalsubjectscreening',
            name='fbg_units',
            field=models.CharField(blank=True, choices=[('mg/dL', 'mg/dL'), ('mmol/L', 'mmol/L (millimoles/L)')], max_length=15, null=True, verbose_name='FBG units'),
        ),
        migrations.AlterField(
            model_name='historicalsubjectscreening',
            name='inclusion_a',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('tbd', 'To be determined')], default='tbd', help_text='system calculated', max_length=15, verbose_name='BMI>30 combined with FBG (6.1 to 6.9 mmol/L)'),
        ),
        migrations.AlterField(
            model_name='historicalsubjectscreening',
            name='inclusion_b',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('tbd', 'To be determined')], default='tbd', help_text='system calculated', max_length=15, verbose_name='BMI>30 combined with OGTT (2 hours) (7.0 to 11.10 mmol/L)'),
        ),
        migrations.AlterField(
            model_name='historicalsubjectscreening',
            name='inclusion_c',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('tbd', 'To be determined')], default='tbd', help_text='system calculated', max_length=15, verbose_name='BMI<=30 combined with FBG (6.3 to 6.9 mmol/L)'),
        ),
        migrations.AlterField(
            model_name='historicalsubjectscreening',
            name='inclusion_d',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('tbd', 'To be determined')], default='tbd', help_text='system calculated', max_length=15, verbose_name='BMI<=30 combined with OGTT (2 hours) (9.0 to 11.10 mmol/L)'),
        ),
        migrations.AlterField(
            model_name='historicalsubjectscreening',
            name='ogtt2_units',
            field=models.CharField(blank=True, choices=[('mg/dL', 'mg/dL'), ('mmol/L', 'mmol/L (millimoles/L)')], max_length=15, null=True, verbose_name='Repeat OGTT Units'),
        ),
        migrations.AlterField(
            model_name='historicalsubjectscreening',
            name='ogtt_units',
            field=models.CharField(blank=True, choices=[('mg/dL', 'mg/dL'), ('mmol/L', 'mmol/L (millimoles/L)')], max_length=15, null=True, verbose_name='OGTT Units'),
        ),
        migrations.AlterField(
            model_name='subjectscreening',
            name='converted_fbg2_value',
            field=models.DecimalField(decimal_places=4, help_text='mmol/L (system converted)', max_digits=8, null=True, verbose_name='Repeat FBG level'),
        ),
        migrations.AlterField(
            model_name='subjectscreening',
            name='converted_ogtt2_value',
            field=models.DecimalField(decimal_places=4, help_text='mmol/L (system converted)', max_digits=8, null=True, verbose_name='Repeat OGTT (2-hours)'),
        ),
        migrations.AlterField(
            model_name='subjectscreening',
            name='converted_ogtt_value',
            field=models.DecimalField(decimal_places=4, help_text='mmol/L (system converted)', max_digits=8, null=True, verbose_name='OGTT (2-hours)'),
        ),
        migrations.AlterField(
            model_name='subjectscreening',
            name='fbg_units',
            field=models.CharField(blank=True, choices=[('mg/dL', 'mg/dL'), ('mmol/L', 'mmol/L (millimoles/L)')], max_length=15, null=True, verbose_name='FBG units'),
        ),
        migrations.AlterField(
            model_name='subjectscreening',
            name='inclusion_a',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('tbd', 'To be determined')], default='tbd', help_text='system calculated', max_length=15, verbose_name='BMI>30 combined with FBG (6.1 to 6.9 mmol/L)'),
        ),
        migrations.AlterField(
            model_name='subjectscreening',
            name='inclusion_b',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('tbd', 'To be determined')], default='tbd', help_text='system calculated', max_length=15, verbose_name='BMI>30 combined with OGTT (2 hours) (7.0 to 11.10 mmol/L)'),
        ),
        migrations.AlterField(
            model_name='subjectscreening',
            name='inclusion_c',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('tbd', 'To be determined')], default='tbd', help_text='system calculated', max_length=15, verbose_name='BMI<=30 combined with FBG (6.3 to 6.9 mmol/L)'),
        ),
        migrations.AlterField(
            model_name='subjectscreening',
            name='inclusion_d',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('tbd', 'To be determined')], default='tbd', help_text='system calculated', max_length=15, verbose_name='BMI<=30 combined with OGTT (2 hours) (9.0 to 11.10 mmol/L)'),
        ),
        migrations.AlterField(
            model_name='subjectscreening',
            name='ogtt2_units',
            field=models.CharField(blank=True, choices=[('mg/dL', 'mg/dL'), ('mmol/L', 'mmol/L (millimoles/L)')], max_length=15, null=True, verbose_name='Repeat OGTT Units'),
        ),
        migrations.AlterField(
            model_name='subjectscreening',
            name='ogtt_units',
            field=models.CharField(blank=True, choices=[('mg/dL', 'mg/dL'), ('mmol/L', 'mmol/L (millimoles/L)')], max_length=15, null=True, verbose_name='OGTT Units'),
        ),
    ]
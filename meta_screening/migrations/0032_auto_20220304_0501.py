# Generated by Django 3.2.11 on 2022-03-04 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meta_screening', '0031_auto_20220304_0448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalscreeningpartone',
            name='ifg_datetime',
            field=models.DateTimeField(blank=True, null=True, verbose_name='<u>Time</u> FBG level measured'),
        ),
        migrations.AlterField(
            model_name='historicalscreeningpartone',
            name='ifg_quantifier',
            field=models.CharField(choices=[('=', '='), ('>', '>'), ('>=', '>='), ('<', '<'), ('<=', '<=')], default='=', max_length=10, verbose_name='FBG quantifier'),
        ),
        migrations.AlterField(
            model_name='historicalscreeningpartone',
            name='ifg_value',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='A `HIGH` reading may be entered as 9999.99', max_digits=8, null=True, verbose_name='FBG level'),
        ),
        migrations.AlterField(
            model_name='historicalscreeningpartthree',
            name='ifg_datetime',
            field=models.DateTimeField(blank=True, null=True, verbose_name='<u>Time</u> FBG level measured'),
        ),
        migrations.AlterField(
            model_name='historicalscreeningpartthree',
            name='ifg_quantifier',
            field=models.CharField(choices=[('=', '='), ('>', '>'), ('>=', '>='), ('<', '<'), ('<=', '<=')], default='=', max_length=10, verbose_name='FBG quantifier'),
        ),
        migrations.AlterField(
            model_name='historicalscreeningpartthree',
            name='ifg_value',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='A `HIGH` reading may be entered as 9999.99', max_digits=8, null=True, verbose_name='FBG level'),
        ),
        migrations.AlterField(
            model_name='historicalscreeningparttwo',
            name='ifg_datetime',
            field=models.DateTimeField(blank=True, null=True, verbose_name='<u>Time</u> FBG level measured'),
        ),
        migrations.AlterField(
            model_name='historicalscreeningparttwo',
            name='ifg_quantifier',
            field=models.CharField(choices=[('=', '='), ('>', '>'), ('>=', '>='), ('<', '<'), ('<=', '<=')], default='=', max_length=10, verbose_name='FBG quantifier'),
        ),
        migrations.AlterField(
            model_name='historicalscreeningparttwo',
            name='ifg_value',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='A `HIGH` reading may be entered as 9999.99', max_digits=8, null=True, verbose_name='FBG level'),
        ),
        migrations.AlterField(
            model_name='historicalsubjectscreening',
            name='ifg_datetime',
            field=models.DateTimeField(blank=True, null=True, verbose_name='<u>Time</u> FBG level measured'),
        ),
        migrations.AlterField(
            model_name='historicalsubjectscreening',
            name='ifg_quantifier',
            field=models.CharField(choices=[('=', '='), ('>', '>'), ('>=', '>='), ('<', '<'), ('<=', '<=')], default='=', max_length=10, verbose_name='FBG quantifier'),
        ),
        migrations.AlterField(
            model_name='historicalsubjectscreening',
            name='ifg_value',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='A `HIGH` reading may be entered as 9999.99', max_digits=8, null=True, verbose_name='FBG level'),
        ),
        migrations.AlterField(
            model_name='subjectscreening',
            name='ifg_datetime',
            field=models.DateTimeField(blank=True, null=True, verbose_name='<u>Time</u> FBG level measured'),
        ),
        migrations.AlterField(
            model_name='subjectscreening',
            name='ifg_quantifier',
            field=models.CharField(choices=[('=', '='), ('>', '>'), ('>=', '>='), ('<', '<'), ('<=', '<=')], default='=', max_length=10, verbose_name='FBG quantifier'),
        ),
        migrations.AlterField(
            model_name='subjectscreening',
            name='ifg_value',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='A `HIGH` reading may be entered as 9999.99', max_digits=8, null=True, verbose_name='FBG level'),
        ),
    ]
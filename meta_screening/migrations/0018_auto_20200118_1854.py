# Generated by Django 2.2.7 on 2020-01-18 15:54

import edc_model.models.fields.blood_pressure
import edc_model.models.fields.height
import edc_model.models.fields.weight
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("meta_screening", "0017_auto_20191213_0314"),
    ]

    operations = [
        migrations.AlterField(
            model_name="historicalscreeningpartone",
            name="dia_blood_pressure",
            field=edc_model.models.fields.blood_pressure.DiastolicPressureField(
                blank=True, null=True
            ),
        ),
        migrations.AlterField(
            model_name="historicalscreeningpartone",
            name="height",
            field=edc_model.models.fields.height.HeightField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="historicalscreeningpartone",
            name="sys_blood_pressure",
            field=edc_model.models.fields.blood_pressure.SystolicPressureField(
                blank=True, null=True
            ),
        ),
        migrations.AlterField(
            model_name="historicalscreeningpartone",
            name="weight",
            field=edc_model.models.fields.weight.WeightField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="historicalscreeningpartthree",
            name="dia_blood_pressure",
            field=edc_model.models.fields.blood_pressure.DiastolicPressureField(
                blank=True, null=True
            ),
        ),
        migrations.AlterField(
            model_name="historicalscreeningpartthree",
            name="height",
            field=edc_model.models.fields.height.HeightField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="historicalscreeningpartthree",
            name="sys_blood_pressure",
            field=edc_model.models.fields.blood_pressure.SystolicPressureField(
                blank=True, null=True
            ),
        ),
        migrations.AlterField(
            model_name="historicalscreeningpartthree",
            name="weight",
            field=edc_model.models.fields.weight.WeightField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="historicalscreeningparttwo",
            name="dia_blood_pressure",
            field=edc_model.models.fields.blood_pressure.DiastolicPressureField(
                blank=True, null=True
            ),
        ),
        migrations.AlterField(
            model_name="historicalscreeningparttwo",
            name="height",
            field=edc_model.models.fields.height.HeightField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="historicalscreeningparttwo",
            name="sys_blood_pressure",
            field=edc_model.models.fields.blood_pressure.SystolicPressureField(
                blank=True, null=True
            ),
        ),
        migrations.AlterField(
            model_name="historicalscreeningparttwo",
            name="weight",
            field=edc_model.models.fields.weight.WeightField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="historicalsubjectscreening",
            name="dia_blood_pressure",
            field=edc_model.models.fields.blood_pressure.DiastolicPressureField(
                blank=True, null=True
            ),
        ),
        migrations.AlterField(
            model_name="historicalsubjectscreening",
            name="height",
            field=edc_model.models.fields.height.HeightField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="historicalsubjectscreening",
            name="sys_blood_pressure",
            field=edc_model.models.fields.blood_pressure.SystolicPressureField(
                blank=True, null=True
            ),
        ),
        migrations.AlterField(
            model_name="historicalsubjectscreening",
            name="weight",
            field=edc_model.models.fields.weight.WeightField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="subjectscreening",
            name="dia_blood_pressure",
            field=edc_model.models.fields.blood_pressure.DiastolicPressureField(
                blank=True, null=True
            ),
        ),
        migrations.AlterField(
            model_name="subjectscreening",
            name="height",
            field=edc_model.models.fields.height.HeightField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="subjectscreening",
            name="sys_blood_pressure",
            field=edc_model.models.fields.blood_pressure.SystolicPressureField(
                blank=True, null=True
            ),
        ),
        migrations.AlterField(
            model_name="subjectscreening",
            name="weight",
            field=edc_model.models.fields.weight.WeightField(blank=True, null=True),
        ),
    ]

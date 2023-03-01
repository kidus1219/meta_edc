# Generated by Django 2.2.6 on 2019-10-24 07:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("meta_prn", "0001_initial")]

    operations = [
        migrations.AlterField(
            model_name="endofstudy",
            name="site",
            field=models.ForeignKey(
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="+",
                to="sites.Site",
            ),
        ),
        migrations.AlterField(
            model_name="losstofollowup",
            name="site",
            field=models.ForeignKey(
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="+",
                to="sites.Site",
            ),
        ),
        migrations.AlterField(
            model_name="onschedule",
            name="site",
            field=models.ForeignKey(
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="+",
                to="sites.Site",
            ),
        ),
        migrations.AlterField(
            model_name="protocoldeviationviolation",
            name="site",
            field=models.ForeignKey(
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="+",
                to="sites.Site",
            ),
        ),
        migrations.AlterField(
            model_name="unblindingrequest",
            name="site",
            field=models.ForeignKey(
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="+",
                to="sites.Site",
            ),
        ),
        migrations.AlterField(
            model_name="unblindingreview",
            name="site",
            field=models.ForeignKey(
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="+",
                to="sites.Site",
            ),
        ),
    ]

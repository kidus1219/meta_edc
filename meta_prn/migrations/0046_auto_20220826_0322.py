# Generated by Django 3.2.13 on 2022-08-26 00:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("meta_prn", "0045_auto_20220826_0258"),
    ]

    operations = [
        migrations.AlterField(
            model_name="endofstudy",
            name="tracking_identifier",
            field=models.CharField(max_length=32, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="historicalendofstudy",
            name="tracking_identifier",
            field=models.CharField(db_index=True, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name="historicallosstofollowup",
            name="tracking_identifier",
            field=models.CharField(db_index=True, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name="historicaloffschedule",
            name="tracking_identifier",
            field=models.CharField(db_index=True, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name="historicaloffschedulepostnatal",
            name="tracking_identifier",
            field=models.CharField(db_index=True, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name="historicaloffschedulepregnancy",
            name="tracking_identifier",
            field=models.CharField(db_index=True, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name="historicaloffstudymedication",
            name="tracking_identifier",
            field=models.CharField(db_index=True, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name="historicalpregnancynotification",
            name="tracking_identifier",
            field=models.CharField(db_index=True, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name="historicalprotocolincident",
            name="tracking_identifier",
            field=models.CharField(db_index=True, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name="historicalsubjecttransfer",
            name="tracking_identifier",
            field=models.CharField(db_index=True, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name="losstofollowup",
            name="tracking_identifier",
            field=models.CharField(max_length=32, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="offschedule",
            name="tracking_identifier",
            field=models.CharField(max_length=32, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="offschedulepostnatal",
            name="tracking_identifier",
            field=models.CharField(max_length=32, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="offschedulepregnancy",
            name="tracking_identifier",
            field=models.CharField(max_length=32, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="offstudymedication",
            name="tracking_identifier",
            field=models.CharField(max_length=32, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="pregnancynotification",
            name="tracking_identifier",
            field=models.CharField(max_length=32, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="protocolincident",
            name="tracking_identifier",
            field=models.CharField(max_length=32, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="subjecttransfer",
            name="tracking_identifier",
            field=models.CharField(max_length=32, null=True, unique=True),
        ),
    ]

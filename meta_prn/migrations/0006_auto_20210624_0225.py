# Generated by Django 3.2.4 on 2021-06-23 23:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("edc_action_item", "0028_auto_20210203_0706"),
        ("meta_prn", "0005_auto_20200524_1944"),
    ]

    operations = [
        migrations.AlterField(
            model_name="endofstudy",
            name="action_item",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="edc_action_item.actionitem",
            ),
        ),
        migrations.AlterField(
            model_name="endofstudy",
            name="parent_action_identifier",
            field=models.CharField(
                blank=True,
                help_text="action identifier that links to parent reference model instance.",
                max_length=30,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="endofstudy",
            name="parent_action_item",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="+",
                to="edc_action_item.actionitem",
            ),
        ),
        migrations.AlterField(
            model_name="endofstudy",
            name="related_action_identifier",
            field=models.CharField(
                blank=True,
                help_text="action identifier that links to related reference model instance.",
                max_length=30,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="endofstudy",
            name="related_action_item",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="+",
                to="edc_action_item.actionitem",
            ),
        ),
        migrations.AlterField(
            model_name="historicalendofstudy",
            name="parent_action_identifier",
            field=models.CharField(
                blank=True,
                help_text="action identifier that links to parent reference model instance.",
                max_length=30,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="historicalendofstudy",
            name="related_action_identifier",
            field=models.CharField(
                blank=True,
                help_text="action identifier that links to related reference model instance.",
                max_length=30,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="historicallosstofollowup",
            name="parent_action_identifier",
            field=models.CharField(
                blank=True,
                help_text="action identifier that links to parent reference model instance.",
                max_length=30,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="historicallosstofollowup",
            name="related_action_identifier",
            field=models.CharField(
                blank=True,
                help_text="action identifier that links to related reference model instance.",
                max_length=30,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="historicalprotocoldeviationviolation",
            name="parent_action_identifier",
            field=models.CharField(
                blank=True,
                help_text="action identifier that links to parent reference model instance.",
                max_length=30,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="historicalprotocoldeviationviolation",
            name="related_action_identifier",
            field=models.CharField(
                blank=True,
                help_text="action identifier that links to related reference model instance.",
                max_length=30,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="historicalunblindingrequest",
            name="parent_action_identifier",
            field=models.CharField(
                blank=True,
                help_text="action identifier that links to parent reference model instance.",
                max_length=30,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="historicalunblindingrequest",
            name="related_action_identifier",
            field=models.CharField(
                blank=True,
                help_text="action identifier that links to related reference model instance.",
                max_length=30,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="historicalunblindingreview",
            name="parent_action_identifier",
            field=models.CharField(
                blank=True,
                help_text="action identifier that links to parent reference model instance.",
                max_length=30,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="historicalunblindingreview",
            name="related_action_identifier",
            field=models.CharField(
                blank=True,
                help_text="action identifier that links to related reference model instance.",
                max_length=30,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="losstofollowup",
            name="action_item",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="edc_action_item.actionitem",
            ),
        ),
        migrations.AlterField(
            model_name="losstofollowup",
            name="parent_action_identifier",
            field=models.CharField(
                blank=True,
                help_text="action identifier that links to parent reference model instance.",
                max_length=30,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="losstofollowup",
            name="parent_action_item",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="+",
                to="edc_action_item.actionitem",
            ),
        ),
        migrations.AlterField(
            model_name="losstofollowup",
            name="related_action_identifier",
            field=models.CharField(
                blank=True,
                help_text="action identifier that links to related reference model instance.",
                max_length=30,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="losstofollowup",
            name="related_action_item",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="+",
                to="edc_action_item.actionitem",
            ),
        ),
        migrations.AlterField(
            model_name="protocoldeviationviolation",
            name="action_item",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="edc_action_item.actionitem",
            ),
        ),
        migrations.AlterField(
            model_name="protocoldeviationviolation",
            name="parent_action_identifier",
            field=models.CharField(
                blank=True,
                help_text="action identifier that links to parent reference model instance.",
                max_length=30,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="protocoldeviationviolation",
            name="parent_action_item",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="+",
                to="edc_action_item.actionitem",
            ),
        ),
        migrations.AlterField(
            model_name="protocoldeviationviolation",
            name="related_action_identifier",
            field=models.CharField(
                blank=True,
                help_text="action identifier that links to related reference model instance.",
                max_length=30,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="protocoldeviationviolation",
            name="related_action_item",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="+",
                to="edc_action_item.actionitem",
            ),
        ),
        migrations.AlterField(
            model_name="unblindingrequest",
            name="action_item",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="edc_action_item.actionitem",
            ),
        ),
        migrations.AlterField(
            model_name="unblindingrequest",
            name="parent_action_identifier",
            field=models.CharField(
                blank=True,
                help_text="action identifier that links to parent reference model instance.",
                max_length=30,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="unblindingrequest",
            name="parent_action_item",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="+",
                to="edc_action_item.actionitem",
            ),
        ),
        migrations.AlterField(
            model_name="unblindingrequest",
            name="related_action_identifier",
            field=models.CharField(
                blank=True,
                help_text="action identifier that links to related reference model instance.",
                max_length=30,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="unblindingrequest",
            name="related_action_item",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="+",
                to="edc_action_item.actionitem",
            ),
        ),
        migrations.AlterField(
            model_name="unblindingreview",
            name="action_item",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="edc_action_item.actionitem",
            ),
        ),
        migrations.AlterField(
            model_name="unblindingreview",
            name="parent_action_identifier",
            field=models.CharField(
                blank=True,
                help_text="action identifier that links to parent reference model instance.",
                max_length=30,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="unblindingreview",
            name="parent_action_item",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="+",
                to="edc_action_item.actionitem",
            ),
        ),
        migrations.AlterField(
            model_name="unblindingreview",
            name="related_action_identifier",
            field=models.CharField(
                blank=True,
                help_text="action identifier that links to related reference model instance.",
                max_length=30,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="unblindingreview",
            name="related_action_item",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="+",
                to="edc_action_item.actionitem",
            ),
        ),
    ]

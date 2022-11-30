# Generated by Django 4.1.2 on 2022-11-30 16:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("meta_subject", "0156_alter_bloodresultsfbc_assay_datetime_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="bloodresultsfbc",
            name="crf_status",
        ),
        migrations.RemoveField(
            model_name="bloodresultsfbc",
            name="crf_status_comments",
        ),
        migrations.RemoveField(
            model_name="historicalbloodresultsfbc",
            name="crf_status",
        ),
        migrations.RemoveField(
            model_name="historicalbloodresultsfbc",
            name="crf_status_comments",
        ),
        migrations.AlterField(
            model_name="bloodresultsfbc",
            name="requisition",
            field=models.ForeignKey(
                blank=True,
                help_text="Start typing the requisition identifier or select one from this visit",
                limit_choices_to={"panel__name": "fbc"},
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="+",
                to="meta_subject.subjectrequisition",
                verbose_name="Requisition",
            ),
        ),
        migrations.AlterField(
            model_name="bloodresultsfbc",
            name="results_abnormal",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No")],
                help_text="Abnormal results at present at baseline or continuing from baseline not included.",
                max_length=25,
                verbose_name="Are any of the above results abnormal?",
            ),
        ),
        migrations.AlterField(
            model_name="bloodresultsfbc",
            name="results_reportable",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No"), ("N/A", "Not applicable")],
                help_text="If YES, this value will open Adverse Event Form. Grade 3 and 4 results present at baseline or continuing from baseline not included",
                max_length=25,
                verbose_name="If any results are abnormal, are results within grade 3 or above?",
            ),
        ),
        migrations.AlterField(
            model_name="bloodresultsglu",
            name="requisition",
            field=models.ForeignKey(
                blank=True,
                help_text="Start typing the requisition identifier or select one from this visit",
                limit_choices_to={"panel__name": "blood_glucose"},
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="+",
                to="meta_subject.subjectrequisition",
                verbose_name="Requisition",
            ),
        ),
        migrations.AlterField(
            model_name="bloodresultsglu",
            name="results_abnormal",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No")],
                help_text="Abnormal results at present at baseline or continuing from baseline not included.",
                max_length=25,
                verbose_name="Are any of the above results abnormal?",
            ),
        ),
        migrations.AlterField(
            model_name="bloodresultsglu",
            name="results_reportable",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No"), ("N/A", "Not applicable")],
                help_text="If YES, this value will open Adverse Event Form. Grade 3 and 4 results present at baseline or continuing from baseline not included",
                max_length=25,
                verbose_name="If any results are abnormal, are results within grade 3 or above?",
            ),
        ),
        migrations.AlterField(
            model_name="bloodresultshba1c",
            name="requisition",
            field=models.ForeignKey(
                blank=True,
                help_text="Start typing the requisition identifier or select one from this visit",
                limit_choices_to={"panel__name": "hba1c"},
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="+",
                to="meta_subject.subjectrequisition",
                verbose_name="Requisition",
            ),
        ),
        migrations.AlterField(
            model_name="bloodresultshba1c",
            name="results_abnormal",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No")],
                help_text="Abnormal results at present at baseline or continuing from baseline not included.",
                max_length=25,
                verbose_name="Are any of the above results abnormal?",
            ),
        ),
        migrations.AlterField(
            model_name="bloodresultshba1c",
            name="results_reportable",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No"), ("N/A", "Not applicable")],
                help_text="If YES, this value will open Adverse Event Form. Grade 3 and 4 results present at baseline or continuing from baseline not included",
                max_length=25,
                verbose_name="If any results are abnormal, are results within grade 3 or above?",
            ),
        ),
        migrations.AlterField(
            model_name="bloodresultsins",
            name="requisition",
            field=models.ForeignKey(
                blank=True,
                help_text="Start typing the requisition identifier or select one from this visit",
                limit_choices_to={"panel__name": "insulin"},
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="+",
                to="meta_subject.subjectrequisition",
                verbose_name="Requisition",
            ),
        ),
        migrations.AlterField(
            model_name="bloodresultsins",
            name="results_abnormal",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No")],
                help_text="Abnormal results at present at baseline or continuing from baseline not included.",
                max_length=25,
                verbose_name="Are any of the above results abnormal?",
            ),
        ),
        migrations.AlterField(
            model_name="bloodresultsins",
            name="results_reportable",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No"), ("N/A", "Not applicable")],
                help_text="If YES, this value will open Adverse Event Form. Grade 3 and 4 results present at baseline or continuing from baseline not included",
                max_length=25,
                verbose_name="If any results are abnormal, are results within grade 3 or above?",
            ),
        ),
        migrations.AlterField(
            model_name="bloodresultslft",
            name="requisition",
            field=models.ForeignKey(
                blank=True,
                help_text="Start typing the requisition identifier or select one from this visit",
                limit_choices_to={"panel__name": "chemistry_lft"},
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="+",
                to="meta_subject.subjectrequisition",
                verbose_name="Requisition",
            ),
        ),
        migrations.AlterField(
            model_name="bloodresultslft",
            name="results_abnormal",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No")],
                help_text="Abnormal results at present at baseline or continuing from baseline not included.",
                max_length=25,
                verbose_name="Are any of the above results abnormal?",
            ),
        ),
        migrations.AlterField(
            model_name="bloodresultslft",
            name="results_reportable",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No"), ("N/A", "Not applicable")],
                help_text="If YES, this value will open Adverse Event Form. Grade 3 and 4 results present at baseline or continuing from baseline not included",
                max_length=25,
                verbose_name="If any results are abnormal, are results within grade 3 or above?",
            ),
        ),
        migrations.AlterField(
            model_name="bloodresultslipid",
            name="requisition",
            field=models.ForeignKey(
                blank=True,
                help_text="Start typing the requisition identifier or select one from this visit",
                limit_choices_to={"panel__name": "chemistry_lipids"},
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="+",
                to="meta_subject.subjectrequisition",
                verbose_name="Requisition",
            ),
        ),
        migrations.AlterField(
            model_name="bloodresultslipid",
            name="results_abnormal",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No")],
                help_text="Abnormal results at present at baseline or continuing from baseline not included.",
                max_length=25,
                verbose_name="Are any of the above results abnormal?",
            ),
        ),
        migrations.AlterField(
            model_name="bloodresultslipid",
            name="results_reportable",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No"), ("N/A", "Not applicable")],
                help_text="If YES, this value will open Adverse Event Form. Grade 3 and 4 results present at baseline or continuing from baseline not included",
                max_length=25,
                verbose_name="If any results are abnormal, are results within grade 3 or above?",
            ),
        ),
        migrations.AlterField(
            model_name="bloodresultsrft",
            name="requisition",
            field=models.ForeignKey(
                blank=True,
                help_text="Start typing the requisition identifier or select one from this visit",
                limit_choices_to={"panel__name": "chemistry_rft"},
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="+",
                to="meta_subject.subjectrequisition",
                verbose_name="Requisition",
            ),
        ),
        migrations.AlterField(
            model_name="bloodresultsrft",
            name="results_abnormal",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No")],
                help_text="Abnormal results at present at baseline or continuing from baseline not included.",
                max_length=25,
                verbose_name="Are any of the above results abnormal?",
            ),
        ),
        migrations.AlterField(
            model_name="bloodresultsrft",
            name="results_reportable",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No"), ("N/A", "Not applicable")],
                help_text="If YES, this value will open Adverse Event Form. Grade 3 and 4 results present at baseline or continuing from baseline not included",
                max_length=25,
                verbose_name="If any results are abnormal, are results within grade 3 or above?",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbloodresultsfbc",
            name="requisition",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                help_text="Start typing the requisition identifier or select one from this visit",
                limit_choices_to={"panel__name": "fbc"},
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="meta_subject.subjectrequisition",
                verbose_name="Requisition",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbloodresultsfbc",
            name="results_abnormal",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No")],
                help_text="Abnormal results at present at baseline or continuing from baseline not included.",
                max_length=25,
                verbose_name="Are any of the above results abnormal?",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbloodresultsfbc",
            name="results_reportable",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No"), ("N/A", "Not applicable")],
                help_text="If YES, this value will open Adverse Event Form. Grade 3 and 4 results present at baseline or continuing from baseline not included",
                max_length=25,
                verbose_name="If any results are abnormal, are results within grade 3 or above?",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbloodresultsglu",
            name="requisition",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                help_text="Start typing the requisition identifier or select one from this visit",
                limit_choices_to={"panel__name": "blood_glucose"},
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="meta_subject.subjectrequisition",
                verbose_name="Requisition",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbloodresultsglu",
            name="results_abnormal",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No")],
                help_text="Abnormal results at present at baseline or continuing from baseline not included.",
                max_length=25,
                verbose_name="Are any of the above results abnormal?",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbloodresultsglu",
            name="results_reportable",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No"), ("N/A", "Not applicable")],
                help_text="If YES, this value will open Adverse Event Form. Grade 3 and 4 results present at baseline or continuing from baseline not included",
                max_length=25,
                verbose_name="If any results are abnormal, are results within grade 3 or above?",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbloodresultshba1c",
            name="requisition",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                help_text="Start typing the requisition identifier or select one from this visit",
                limit_choices_to={"panel__name": "hba1c"},
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="meta_subject.subjectrequisition",
                verbose_name="Requisition",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbloodresultshba1c",
            name="results_abnormal",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No")],
                help_text="Abnormal results at present at baseline or continuing from baseline not included.",
                max_length=25,
                verbose_name="Are any of the above results abnormal?",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbloodresultshba1c",
            name="results_reportable",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No"), ("N/A", "Not applicable")],
                help_text="If YES, this value will open Adverse Event Form. Grade 3 and 4 results present at baseline or continuing from baseline not included",
                max_length=25,
                verbose_name="If any results are abnormal, are results within grade 3 or above?",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbloodresultsins",
            name="requisition",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                help_text="Start typing the requisition identifier or select one from this visit",
                limit_choices_to={"panel__name": "insulin"},
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="meta_subject.subjectrequisition",
                verbose_name="Requisition",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbloodresultsins",
            name="results_abnormal",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No")],
                help_text="Abnormal results at present at baseline or continuing from baseline not included.",
                max_length=25,
                verbose_name="Are any of the above results abnormal?",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbloodresultsins",
            name="results_reportable",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No"), ("N/A", "Not applicable")],
                help_text="If YES, this value will open Adverse Event Form. Grade 3 and 4 results present at baseline or continuing from baseline not included",
                max_length=25,
                verbose_name="If any results are abnormal, are results within grade 3 or above?",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbloodresultslft",
            name="requisition",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                help_text="Start typing the requisition identifier or select one from this visit",
                limit_choices_to={"panel__name": "chemistry_lft"},
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="meta_subject.subjectrequisition",
                verbose_name="Requisition",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbloodresultslft",
            name="results_abnormal",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No")],
                help_text="Abnormal results at present at baseline or continuing from baseline not included.",
                max_length=25,
                verbose_name="Are any of the above results abnormal?",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbloodresultslft",
            name="results_reportable",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No"), ("N/A", "Not applicable")],
                help_text="If YES, this value will open Adverse Event Form. Grade 3 and 4 results present at baseline or continuing from baseline not included",
                max_length=25,
                verbose_name="If any results are abnormal, are results within grade 3 or above?",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbloodresultslipid",
            name="requisition",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                help_text="Start typing the requisition identifier or select one from this visit",
                limit_choices_to={"panel__name": "chemistry_lipids"},
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="meta_subject.subjectrequisition",
                verbose_name="Requisition",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbloodresultslipid",
            name="results_abnormal",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No")],
                help_text="Abnormal results at present at baseline or continuing from baseline not included.",
                max_length=25,
                verbose_name="Are any of the above results abnormal?",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbloodresultslipid",
            name="results_reportable",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No"), ("N/A", "Not applicable")],
                help_text="If YES, this value will open Adverse Event Form. Grade 3 and 4 results present at baseline or continuing from baseline not included",
                max_length=25,
                verbose_name="If any results are abnormal, are results within grade 3 or above?",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbloodresultsrft",
            name="requisition",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                help_text="Start typing the requisition identifier or select one from this visit",
                limit_choices_to={"panel__name": "chemistry_rft"},
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="meta_subject.subjectrequisition",
                verbose_name="Requisition",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbloodresultsrft",
            name="results_abnormal",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No")],
                help_text="Abnormal results at present at baseline or continuing from baseline not included.",
                max_length=25,
                verbose_name="Are any of the above results abnormal?",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbloodresultsrft",
            name="results_reportable",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No"), ("N/A", "Not applicable")],
                help_text="If YES, this value will open Adverse Event Form. Grade 3 and 4 results present at baseline or continuing from baseline not included",
                max_length=25,
                verbose_name="If any results are abnormal, are results within grade 3 or above?",
            ),
        ),
    ]

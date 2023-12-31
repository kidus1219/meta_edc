# Generated by Django 3.0.6 on 2020-05-27 18:55

import uuid

import _socket
import django.contrib.sites.managers
import django.core.validators
import django.db.models.deletion
import django_audit_fields.fields.hostname_modification_field
import django_audit_fields.fields.userfield
import django_audit_fields.fields.uuid_auto_field
import django_audit_fields.models.audit_model_mixin
import django_revision.revision_field
import edc_model.models.fields.other_charfield
import edc_model.validators.date
import edc_protocol.validators
import edc_utils.date
import edc_visit_tracking.managers
import simple_history.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("edc_action_item", "0024_auto_20191024_1000"),
        ("sites", "0002_alter_domain_unique"),
        ("meta_lists", "0007_auto_20200516_2356"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("meta_subject", "0039_auto_20200524_1944"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="bloodresultsfbc",
            options={
                "default_permissions": (
                    "add",
                    "change",
                    "delete",
                    "view",
                    "export",
                    "import",
                ),
                "get_latest_by": "modified",
                "ordering": ("-modified", "-created"),
                "verbose_name": "Blood Result: FBC",
                "verbose_name_plural": "Blood Results: FBC",
            },
        ),
        migrations.AlterModelOptions(
            name="bloodresultsglu",
            options={
                "default_permissions": (
                    "add",
                    "change",
                    "delete",
                    "view",
                    "export",
                    "import",
                ),
                "get_latest_by": "modified",
                "ordering": ("-modified", "-created"),
                "verbose_name": "Blood Result: Glucose",
                "verbose_name_plural": "Blood Results: Glucose",
            },
        ),
        migrations.AlterModelOptions(
            name="bloodresultshba1c",
            options={
                "default_permissions": (
                    "add",
                    "change",
                    "delete",
                    "view",
                    "export",
                    "import",
                ),
                "get_latest_by": "modified",
                "ordering": ("-modified", "-created"),
                "verbose_name": "Blood Result: HbA1c",
                "verbose_name_plural": "Blood Results: HbA1c",
            },
        ),
        migrations.AlterModelOptions(
            name="bloodresultslft",
            options={
                "default_permissions": (
                    "add",
                    "change",
                    "delete",
                    "view",
                    "export",
                    "import",
                ),
                "get_latest_by": "modified",
                "ordering": ("-modified", "-created"),
                "verbose_name": "Blood Result: LFT",
                "verbose_name_plural": "Blood Results: LFT",
            },
        ),
        migrations.AlterModelOptions(
            name="bloodresultslipid",
            options={
                "default_permissions": (
                    "add",
                    "change",
                    "delete",
                    "view",
                    "export",
                    "import",
                ),
                "get_latest_by": "modified",
                "ordering": ("-modified", "-created"),
                "verbose_name": "Blood Result: Lipids",
                "verbose_name_plural": "Blood Results: Lipids",
            },
        ),
        migrations.AlterModelOptions(
            name="bloodresultsrft",
            options={
                "default_permissions": (
                    "add",
                    "change",
                    "delete",
                    "view",
                    "export",
                    "import",
                ),
                "get_latest_by": "modified",
                "ordering": ("-modified", "-created"),
                "verbose_name": "Blood Result: RFT",
                "verbose_name_plural": "Blood Results: RFT",
            },
        ),
        migrations.AlterModelOptions(
            name="complications",
            options={
                "default_permissions": (
                    "add",
                    "change",
                    "delete",
                    "view",
                    "export",
                    "import",
                ),
                "get_latest_by": "modified",
                "ordering": ("-modified", "-created"),
                "verbose_name": "Presence of Complications",
                "verbose_name_plural": "Presence of Complications",
            },
        ),
        migrations.AlterModelOptions(
            name="followup",
            options={
                "default_permissions": (
                    "add",
                    "change",
                    "delete",
                    "view",
                    "export",
                    "import",
                ),
                "get_latest_by": "modified",
                "ordering": ("-modified", "-created"),
                "verbose_name": "Clinic follow up: Examination",
                "verbose_name_plural": "Clinic follow up: Examination",
            },
        ),
        migrations.AlterModelOptions(
            name="followupvitals",
            options={
                "default_permissions": (
                    "add",
                    "change",
                    "delete",
                    "view",
                    "export",
                    "import",
                ),
                "get_latest_by": "modified",
                "ordering": ("-modified", "-created"),
                "verbose_name": "Clinic follow up: Vitals",
                "verbose_name_plural": "Clinic follow ups: Vitals",
            },
        ),
        migrations.AlterModelOptions(
            name="glucose",
            options={
                "default_permissions": (
                    "add",
                    "change",
                    "delete",
                    "view",
                    "export",
                    "import",
                ),
                "get_latest_by": "modified",
                "ordering": ("-modified", "-created"),
                "verbose_name": "Glucose (IFG, OGTT)",
                "verbose_name_plural": "Glucose (IFG, OGTT)",
            },
        ),
        migrations.AlterModelOptions(
            name="healtheconomics",
            options={
                "default_permissions": (
                    "add",
                    "change",
                    "delete",
                    "view",
                    "export",
                    "import",
                ),
                "get_latest_by": "modified",
                "ordering": ("-modified", "-created"),
                "verbose_name": "Health Economics",
                "verbose_name_plural": "Health Economics",
            },
        ),
        migrations.AlterModelOptions(
            name="malariatest",
            options={
                "default_permissions": (
                    "add",
                    "change",
                    "delete",
                    "view",
                    "export",
                    "import",
                ),
                "get_latest_by": "modified",
                "ordering": ("-modified", "-created"),
                "verbose_name": "Malaria Test",
            },
        ),
        migrations.AlterModelOptions(
            name="medicationadherence",
            options={
                "default_permissions": (
                    "add",
                    "change",
                    "delete",
                    "view",
                    "export",
                    "import",
                ),
                "get_latest_by": "modified",
                "ordering": ("-modified", "-created"),
                "verbose_name": "Medication Adherence",
                "verbose_name_plural": "Medication Adherence",
            },
        ),
        migrations.AlterModelOptions(
            name="patienthistory",
            options={
                "default_permissions": (
                    "add",
                    "change",
                    "delete",
                    "view",
                    "export",
                    "import",
                ),
                "get_latest_by": "modified",
                "ordering": ("-modified", "-created"),
                "verbose_name": "Patient History",
                "verbose_name_plural": "Patient History",
            },
        ),
        migrations.AlterModelOptions(
            name="physicalexam",
            options={
                "default_permissions": (
                    "add",
                    "change",
                    "delete",
                    "view",
                    "export",
                    "import",
                ),
                "get_latest_by": "modified",
                "ordering": ("-modified", "-created"),
                "verbose_name": "Physical Exam",
                "verbose_name_plural": "Physical Exams",
            },
        ),
        migrations.AlterModelOptions(
            name="subjectrequisition",
            options={
                "default_permissions": (
                    "add",
                    "change",
                    "delete",
                    "view",
                    "export",
                    "import",
                ),
                "get_latest_by": "modified",
                "ordering": ("-modified", "-created"),
            },
        ),
        migrations.AlterModelOptions(
            name="subjectvisit",
            options={
                "default_permissions": (
                    "add",
                    "change",
                    "delete",
                    "view",
                    "export",
                    "import",
                ),
                "get_latest_by": "modified",
                "ordering": (
                    "subject_identifier",
                    "visit_schedule_name",
                    "schedule_name",
                    "visit_code",
                    "visit_code_sequence",
                    "report_datetime",
                ),
            },
        ),
        migrations.AlterModelOptions(
            name="urinedipsticktest",
            options={
                "default_permissions": (
                    "add",
                    "change",
                    "delete",
                    "view",
                    "export",
                    "import",
                ),
                "get_latest_by": "modified",
                "ordering": ("-modified", "-created"),
                "verbose_name": "Urine Dipstick Test",
            },
        ),
        migrations.AddField(
            model_name="followup",
            name="action_identifier",
            field=models.CharField(max_length=50, null=True, unique=True),
        ),
        migrations.AddField(
            model_name="followup",
            name="action_item",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="edc_action_item.ActionItem",
            ),
        ),
        migrations.AddField(
            model_name="followup",
            name="action_item_reason",
            field=models.TextField(editable=False, null=True),
        ),
        migrations.AddField(
            model_name="followup",
            name="any_other_problems_sae_grade",
            field=models.CharField(
                choices=[("3", "Grade 3"), ("4", "Grade 4"), ("N/A", "Not applicable")],
                default="N/A",
                help_text="If YES, grade 3 or 4, submit Serious Adverse Event form",
                max_length=25,
                verbose_name="If YES, what grade?",
            ),
        ),
        migrations.AddField(
            model_name="followup",
            name="parent_action_identifier",
            field=models.CharField(
                help_text="action identifier that links to parent reference model instance.",
                max_length=30,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="followup",
            name="parent_action_item",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="+",
                to="edc_action_item.ActionItem",
            ),
        ),
        migrations.AddField(
            model_name="followup",
            name="related_action_identifier",
            field=models.CharField(
                help_text="action identifier that links to related reference model instance.",
                max_length=30,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="followup",
            name="related_action_item",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="+",
                to="edc_action_item.ActionItem",
            ),
        ),
        migrations.AddField(
            model_name="followup",
            name="tracking_identifier",
            field=models.CharField(max_length=30, null=True, unique=True),
        ),
        migrations.AddField(
            model_name="historicalfollowup",
            name="action_identifier",
            field=models.CharField(db_index=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="historicalfollowup",
            name="action_item",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="edc_action_item.ActionItem",
            ),
        ),
        migrations.AddField(
            model_name="historicalfollowup",
            name="action_item_reason",
            field=models.TextField(editable=False, null=True),
        ),
        migrations.AddField(
            model_name="historicalfollowup",
            name="any_other_problems_sae_grade",
            field=models.CharField(
                choices=[("3", "Grade 3"), ("4", "Grade 4"), ("N/A", "Not applicable")],
                default="N/A",
                help_text="If YES, grade 3 or 4, submit Serious Adverse Event form",
                max_length=25,
                verbose_name="If YES, what grade?",
            ),
        ),
        migrations.AddField(
            model_name="historicalfollowup",
            name="parent_action_identifier",
            field=models.CharField(
                help_text="action identifier that links to parent reference model instance.",
                max_length=30,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="historicalfollowup",
            name="parent_action_item",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="edc_action_item.ActionItem",
            ),
        ),
        migrations.AddField(
            model_name="historicalfollowup",
            name="related_action_identifier",
            field=models.CharField(
                help_text="action identifier that links to related reference model instance.",
                max_length=30,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="historicalfollowup",
            name="related_action_item",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="edc_action_item.ActionItem",
            ),
        ),
        migrations.AddField(
            model_name="historicalfollowup",
            name="tracking_identifier",
            field=models.CharField(db_index=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name="followup",
            name="any_other_problems_sae",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No")],
                max_length=25,
                verbose_name="Does this event constitute an Adverse Event?",
            ),
        ),
        migrations.AlterField(
            model_name="historicalfollowup",
            name="any_other_problems_sae",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No")],
                max_length=25,
                verbose_name="Does this event constitute an Adverse Event?",
            ),
        ),
        migrations.AlterField(
            model_name="historicalmedicationadherence",
            name="other_missed_pill_reason",
            field=edc_model.models.fields.other_charfield.OtherCharField(
                blank=True,
                max_length=35,
                null=True,
                verbose_name="If other, please specify ...",
            ),
        ),
        migrations.AlterField(
            model_name="medicationadherence",
            name="other_missed_pill_reason",
            field=edc_model.models.fields.other_charfield.OtherCharField(
                blank=True,
                max_length=35,
                null=True,
                verbose_name="If other, please specify ...",
            ),
        ),
    ]

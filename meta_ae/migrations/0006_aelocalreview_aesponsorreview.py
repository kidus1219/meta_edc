# Generated by Django 3.2.4 on 2021-07-09 17:56

import _socket
import django.db.models.deletion
import django_audit_fields.fields.hostname_modification_field
import django_audit_fields.fields.userfield
import django_audit_fields.fields.uuid_auto_field
import django_audit_fields.models.audit_model_mixin
import django_revision.revision_field
import edc_model.models.fields.other_charfield
import edc_model.validators.date
import edc_utils.date
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("edc_adverse_event", "0006_auto_20210425_1628"),
        ("meta_ae", "0005_auto_20210624_0225"),
    ]

    operations = [
        migrations.CreateModel(
            name="AeSponsorReview",
            fields=[
                (
                    "revision",
                    django_revision.revision_field.RevisionField(
                        blank=True,
                        editable=False,
                        help_text="System field. Git repository tag:branch:commit.",
                        max_length=75,
                        null=True,
                        verbose_name="Revision",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(
                        blank=True,
                        default=django_audit_fields.models.audit_model_mixin.utcnow,
                    ),
                ),
                (
                    "modified",
                    models.DateTimeField(
                        blank=True,
                        default=django_audit_fields.models.audit_model_mixin.utcnow,
                    ),
                ),
                (
                    "user_created",
                    django_audit_fields.fields.userfield.UserField(
                        blank=True,
                        help_text="Updated by admin.save_model",
                        max_length=50,
                        verbose_name="user created",
                    ),
                ),
                (
                    "user_modified",
                    django_audit_fields.fields.userfield.UserField(
                        blank=True,
                        help_text="Updated by admin.save_model",
                        max_length=50,
                        verbose_name="user modified",
                    ),
                ),
                (
                    "hostname_created",
                    models.CharField(
                        blank=True,
                        default=_socket.gethostname,
                        help_text="System field. (modified on create only)",
                        max_length=60,
                    ),
                ),
                (
                    "hostname_modified",
                    django_audit_fields.fields.hostname_modification_field.HostnameModificationField(
                        blank=True,
                        help_text="System field. (modified on every save)",
                        max_length=50,
                    ),
                ),
                ("device_created", models.CharField(blank=True, max_length=10)),
                ("device_modified", models.CharField(blank=True, max_length=10)),
                (
                    "id",
                    django_audit_fields.fields.uuid_auto_field.UUIDAutoField(
                        blank=True,
                        editable=False,
                        help_text="System auto field. UUID primary key.",
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "report_datetime",
                    models.DateTimeField(
                        default=edc_utils.date.get_utcnow,
                        validators=[edc_model.validators.date.datetime_not_future],
                        verbose_name="Report date and time",
                    ),
                ),
                (
                    "clinical_review_datetime",
                    models.DateTimeField(
                        blank=True,
                        null=True,
                        validators=[edc_model.validators.date.datetime_not_future],
                        verbose_name="Date and time of clinical review: ",
                    ),
                ),
                (
                    "ae_classification_other",
                    edc_model.models.fields.other_charfield.OtherCharField(
                        blank=True,
                        max_length=250,
                        null=True,
                        verbose_name="If other, please specify ...",
                    ),
                ),
                (
                    "ae_type",
                    models.CharField(
                        choices=[
                            ("sae", "Serious Adverse Event / Reaction"),
                            ("aesi", "Adverse Event of Special Interest"),
                            ("susar", "Serious Unexpected Adverse Reaction"),
                        ],
                        max_length=25,
                        verbose_name="Type of event",
                    ),
                ),
                (
                    "study_drug_relation",
                    models.CharField(
                        choices=[
                            ("not_related", "Not related"),
                            ("unlikely_related", "Unlikely related"),
                            ("possibly_related", "Possibly related"),
                            ("probably_related", "Probably related"),
                            ("definitely_related", "Definitely related"),
                            ("N/A", "Not applicable"),
                        ],
                        max_length=25,
                        null=True,
                        verbose_name="Relationship to study drug:",
                    ),
                ),
                (
                    "ae_expected",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")],
                        max_length=25,
                        null=True,
                        verbose_name="Based on the protocol, do you believe this event is expected?",
                    ),
                ),
                (
                    "ae_action_required",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")],
                        max_length=25,
                        null=True,
                        verbose_name="If unexpected, do you believe further action is required?",
                    ),
                ),
                (
                    "investigator_comments",
                    models.TextField(
                        blank=True,
                        null=True,
                        verbose_name="This Clinical Reviewer's comments:",
                    ),
                ),
                (
                    "original_report_agreed",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")],
                        help_text="If No, explain in the narrative below",
                        max_length=15,
                        null=True,
                        verbose_name="Does this Clinical Reviewer agree with the original AE report?",
                    ),
                ),
                (
                    "narrative",
                    models.TextField(blank=True, null=True, verbose_name="Narrative"),
                ),
                (
                    "officials_notified",
                    models.DateTimeField(
                        blank=True,
                        null=True,
                        validators=[edc_model.validators.date.datetime_not_future],
                        verbose_name="Date and time regulatory authorities notified",
                    ),
                ),
                (
                    "ae_classification",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="edc_adverse_event.aeclassification",
                        verbose_name="Adverse Event (AE) Classification",
                    ),
                ),
                (
                    "ae_initial",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="meta_ae.aeinitial",
                    ),
                ),
            ],
            options={
                "verbose_name": "AE Sponsor Review",
            },
        ),
        migrations.CreateModel(
            name="AeLocalReview",
            fields=[
                (
                    "revision",
                    django_revision.revision_field.RevisionField(
                        blank=True,
                        editable=False,
                        help_text="System field. Git repository tag:branch:commit.",
                        max_length=75,
                        null=True,
                        verbose_name="Revision",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(
                        blank=True,
                        default=django_audit_fields.models.audit_model_mixin.utcnow,
                    ),
                ),
                (
                    "modified",
                    models.DateTimeField(
                        blank=True,
                        default=django_audit_fields.models.audit_model_mixin.utcnow,
                    ),
                ),
                (
                    "user_created",
                    django_audit_fields.fields.userfield.UserField(
                        blank=True,
                        help_text="Updated by admin.save_model",
                        max_length=50,
                        verbose_name="user created",
                    ),
                ),
                (
                    "user_modified",
                    django_audit_fields.fields.userfield.UserField(
                        blank=True,
                        help_text="Updated by admin.save_model",
                        max_length=50,
                        verbose_name="user modified",
                    ),
                ),
                (
                    "hostname_created",
                    models.CharField(
                        blank=True,
                        default=_socket.gethostname,
                        help_text="System field. (modified on create only)",
                        max_length=60,
                    ),
                ),
                (
                    "hostname_modified",
                    django_audit_fields.fields.hostname_modification_field.HostnameModificationField(
                        blank=True,
                        help_text="System field. (modified on every save)",
                        max_length=50,
                    ),
                ),
                ("device_created", models.CharField(blank=True, max_length=10)),
                ("device_modified", models.CharField(blank=True, max_length=10)),
                (
                    "id",
                    django_audit_fields.fields.uuid_auto_field.UUIDAutoField(
                        blank=True,
                        editable=False,
                        help_text="System auto field. UUID primary key.",
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "report_datetime",
                    models.DateTimeField(
                        default=edc_utils.date.get_utcnow,
                        validators=[edc_model.validators.date.datetime_not_future],
                        verbose_name="Report date and time",
                    ),
                ),
                (
                    "clinical_review_datetime",
                    models.DateTimeField(
                        blank=True,
                        null=True,
                        validators=[edc_model.validators.date.datetime_not_future],
                        verbose_name="Date and time of clinical review: ",
                    ),
                ),
                (
                    "ae_classification_other",
                    edc_model.models.fields.other_charfield.OtherCharField(
                        blank=True,
                        max_length=250,
                        null=True,
                        verbose_name="If other, please specify ...",
                    ),
                ),
                (
                    "ae_type",
                    models.CharField(
                        choices=[
                            ("sae", "Serious Adverse Event / Reaction"),
                            ("aesi", "Adverse Event of Special Interest"),
                            ("susar", "Serious Unexpected Adverse Reaction"),
                        ],
                        max_length=25,
                        verbose_name="Type of event",
                    ),
                ),
                (
                    "study_drug_relation",
                    models.CharField(
                        choices=[
                            ("not_related", "Not related"),
                            ("unlikely_related", "Unlikely related"),
                            ("possibly_related", "Possibly related"),
                            ("probably_related", "Probably related"),
                            ("definitely_related", "Definitely related"),
                            ("N/A", "Not applicable"),
                        ],
                        max_length=25,
                        null=True,
                        verbose_name="Relationship to study drug:",
                    ),
                ),
                (
                    "ae_expected",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")],
                        max_length=25,
                        null=True,
                        verbose_name="Based on the protocol, do you believe this event is expected?",
                    ),
                ),
                (
                    "ae_action_required",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")],
                        max_length=25,
                        null=True,
                        verbose_name="If unexpected, do you believe further action is required?",
                    ),
                ),
                (
                    "investigator_comments",
                    models.TextField(
                        blank=True,
                        null=True,
                        verbose_name="This Clinical Reviewer's comments:",
                    ),
                ),
                (
                    "original_report_agreed",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")],
                        help_text="If No, explain in the narrative below",
                        max_length=15,
                        null=True,
                        verbose_name="Does this Clinical Reviewer agree with the original AE report?",
                    ),
                ),
                (
                    "narrative",
                    models.TextField(blank=True, null=True, verbose_name="Narrative"),
                ),
                (
                    "officials_notified",
                    models.DateTimeField(
                        blank=True,
                        null=True,
                        validators=[edc_model.validators.date.datetime_not_future],
                        verbose_name="Date and time regulatory authorities notified",
                    ),
                ),
                (
                    "ae_classification",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="edc_adverse_event.aeclassification",
                        verbose_name="Adverse Event (AE) Classification",
                    ),
                ),
                (
                    "ae_initial",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="meta_ae.aeinitial",
                    ),
                ),
            ],
            options={
                "verbose_name": "AE Local Review",
            },
        ),
    ]

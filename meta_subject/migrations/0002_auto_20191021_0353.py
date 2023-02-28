# Generated by Django 2.2.6 on 2019-10-21 00:53

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
import edc_model.validators.date
import edc_protocol.validators
import edc_utils.date
import edc_visit_tracking.managers
import simple_history.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("sites", "0002_alter_domain_unique"),
        ("meta_subject", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="historicalpatienthistory", name="abdominal_tenderness"
        ),
        migrations.RemoveField(
            model_name="historicalpatienthistory", name="dia_blood_pressure"
        ),
        migrations.RemoveField(
            model_name="historicalpatienthistory", name="has_abdominal_tenderness"
        ),
        migrations.RemoveField(
            model_name="historicalpatienthistory", name="has_enlarged_liver"
        ),
        migrations.RemoveField(model_name="historicalpatienthistory", name="heart_rate"),
        migrations.RemoveField(
            model_name="historicalpatienthistory", name="irregular_heartbeat"
        ),
        migrations.RemoveField(
            model_name="historicalpatienthistory", name="is_heartbeat_regular"
        ),
        migrations.RemoveField(model_name="historicalpatienthistory", name="jaundice"),
        migrations.RemoveField(
            model_name="historicalpatienthistory", name="peripheral_oedema"
        ),
        migrations.RemoveField(model_name="historicalpatienthistory", name="respiratory_rate"),
        migrations.RemoveField(
            model_name="historicalpatienthistory", name="sys_blood_pressure"
        ),
        migrations.RemoveField(model_name="historicalpatienthistory", name="temperature"),
        migrations.RemoveField(
            model_name="historicalpatienthistory", name="waist_circumference"
        ),
        migrations.RemoveField(model_name="historicalpatienthistory", name="weight"),
        migrations.RemoveField(model_name="patienthistory", name="abdominal_tenderness"),
        migrations.RemoveField(model_name="patienthistory", name="dia_blood_pressure"),
        migrations.RemoveField(model_name="patienthistory", name="has_abdominal_tenderness"),
        migrations.RemoveField(model_name="patienthistory", name="has_enlarged_liver"),
        migrations.RemoveField(model_name="patienthistory", name="heart_rate"),
        migrations.RemoveField(model_name="patienthistory", name="irregular_heartbeat"),
        migrations.RemoveField(model_name="patienthistory", name="is_heartbeat_regular"),
        migrations.RemoveField(model_name="patienthistory", name="jaundice"),
        migrations.RemoveField(model_name="patienthistory", name="peripheral_oedema"),
        migrations.RemoveField(model_name="patienthistory", name="respiratory_rate"),
        migrations.RemoveField(model_name="patienthistory", name="sys_blood_pressure"),
        migrations.RemoveField(model_name="patienthistory", name="temperature"),
        migrations.RemoveField(model_name="patienthistory", name="waist_circumference"),
        migrations.RemoveField(model_name="patienthistory", name="weight"),
        migrations.AddField(
            model_name="followupvitals",
            name="oxygen_saturation",
            field=models.IntegerField(
                editable=False,
                help_text="%",
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(999),
                ],
                verbose_name="Oxygen saturation:",
            ),
        ),
        migrations.AddField(
            model_name="historicalfollowupvitals",
            name="oxygen_saturation",
            field=models.IntegerField(
                editable=False,
                help_text="%",
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(999),
                ],
                verbose_name="Oxygen saturation:",
            ),
        ),
        migrations.AlterField(
            model_name="followupvitals",
            name="respiratory_rate",
            field=models.IntegerField(
                editable=False,
                help_text="breaths/min",
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(6),
                    django.core.validators.MaxValueValidator(50),
                ],
                verbose_name="Respiratory rate:",
            ),
        ),
        migrations.AlterField(
            model_name="historicalfollowupvitals",
            name="respiratory_rate",
            field=models.IntegerField(
                editable=False,
                help_text="breaths/min",
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(6),
                    django.core.validators.MaxValueValidator(50),
                ],
                verbose_name="Respiratory rate:",
            ),
        ),
        migrations.CreateModel(
            name="PhysicalExam",
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
                    "consent_model",
                    models.CharField(editable=False, max_length=50, null=True),
                ),
                (
                    "consent_version",
                    models.CharField(editable=False, max_length=10, null=True),
                ),
                (
                    "report_datetime",
                    models.DateTimeField(
                        default=edc_utils.date.get_utcnow,
                        help_text="If reporting today, use today's date/time, otherwise use the date/time this information was reported.",
                        validators=[
                            edc_protocol.validators.datetime_not_before_study_start,
                            edc_model.validators.date.datetime_not_future,
                        ],
                        verbose_name="Report Date",
                    ),
                ),
                (
                    "weight",
                    models.DecimalField(
                        decimal_places=1,
                        help_text="kg",
                        max_digits=4,
                        validators=[
                            django.core.validators.MinValueValidator(20),
                            django.core.validators.MaxValueValidator(150),
                        ],
                        verbose_name="Weight:",
                    ),
                ),
                (
                    "sys_blood_pressure",
                    models.IntegerField(
                        help_text="in mm. format SYS, e.g. 120",
                        validators=[
                            django.core.validators.MinValueValidator(50),
                            django.core.validators.MaxValueValidator(220),
                        ],
                        verbose_name="Blood pressure: systolic",
                    ),
                ),
                (
                    "dia_blood_pressure",
                    models.IntegerField(
                        help_text="in Hg. format DIA, e.g. 80",
                        validators=[
                            django.core.validators.MinValueValidator(20),
                            django.core.validators.MaxValueValidator(150),
                        ],
                        verbose_name="Blood pressure: diastolic",
                    ),
                ),
                (
                    "heart_rate",
                    models.IntegerField(
                        help_text="BPM",
                        validators=[
                            django.core.validators.MinValueValidator(30),
                            django.core.validators.MaxValueValidator(200),
                        ],
                        verbose_name="Heart rate:",
                    ),
                ),
                (
                    "respiratory_rate",
                    models.IntegerField(
                        editable=False,
                        help_text="breaths/min",
                        null=True,
                        validators=[
                            django.core.validators.MinValueValidator(6),
                            django.core.validators.MaxValueValidator(50),
                        ],
                        verbose_name="Respiratory rate:",
                    ),
                ),
                (
                    "oxygen_saturation",
                    models.IntegerField(
                        editable=False,
                        help_text="%",
                        null=True,
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(999),
                        ],
                        verbose_name="Oxygen saturation:",
                    ),
                ),
                (
                    "temperature",
                    models.DecimalField(
                        decimal_places=1,
                        help_text="in degrees Celcius",
                        max_digits=3,
                        validators=[
                            django.core.validators.MinValueValidator(30),
                            django.core.validators.MaxValueValidator(45),
                        ],
                        verbose_name="Temperature:",
                    ),
                ),
                (
                    "is_heartbeat_regular",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")],
                        max_length=15,
                        verbose_name="Is the heart beat regular?",
                    ),
                ),
                (
                    "irregular_heartbeat",
                    models.TextField(
                        blank=True,
                        null=True,
                        verbose_name="If the heartbeat is NOT regular, please describe",
                    ),
                ),
                (
                    "waist_circumference",
                    models.DecimalField(
                        decimal_places=1,
                        help_text="in centimeters",
                        max_digits=5,
                        validators=[
                            django.core.validators.MinValueValidator(50.0),
                            django.core.validators.MaxValueValidator(175.0),
                        ],
                        verbose_name="Waist circumference",
                    ),
                ),
                (
                    "jaundice",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")],
                        max_length=15,
                        verbose_name="Jaundice",
                    ),
                ),
                (
                    "peripheral_oedema",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")],
                        max_length=15,
                        verbose_name="Presence of peripheral oedema",
                    ),
                ),
                (
                    "has_abdominal_tenderness",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")],
                        max_length=15,
                        verbose_name="Abdominal tenderness on palpation",
                    ),
                ),
                (
                    "abdominal_tenderness",
                    models.TextField(
                        blank=True,
                        null=True,
                        verbose_name="If YES, abdominal tenderness, please describe",
                    ),
                ),
                (
                    "has_enlarged_liver",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")],
                        max_length=15,
                        verbose_name="Enlarged liver on palpation",
                    ),
                ),
                (
                    "site",
                    models.ForeignKey(
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="sites.Site",
                    ),
                ),
                (
                    "subject_visit",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="meta_subject.SubjectVisit",
                    ),
                ),
            ],
            options={
                "verbose_name": "Patient History",
                "verbose_name_plural": "Patient History",
                "abstract": False,
            },
            managers=[
                ("on_site", django.contrib.sites.managers.CurrentSiteManager()),
                ("objects", edc_visit_tracking.managers.CrfModelManager()),
            ],
        ),
        migrations.CreateModel(
            name="HistoricalPhysicalExam",
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
                        db_index=True,
                        editable=False,
                        help_text="System auto field. UUID primary key.",
                    ),
                ),
                (
                    "consent_model",
                    models.CharField(editable=False, max_length=50, null=True),
                ),
                (
                    "consent_version",
                    models.CharField(editable=False, max_length=10, null=True),
                ),
                (
                    "report_datetime",
                    models.DateTimeField(
                        default=edc_utils.date.get_utcnow,
                        help_text="If reporting today, use today's date/time, otherwise use the date/time this information was reported.",
                        validators=[
                            edc_protocol.validators.datetime_not_before_study_start,
                            edc_model.validators.date.datetime_not_future,
                        ],
                        verbose_name="Report Date",
                    ),
                ),
                (
                    "history_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "weight",
                    models.DecimalField(
                        decimal_places=1,
                        help_text="kg",
                        max_digits=4,
                        validators=[
                            django.core.validators.MinValueValidator(20),
                            django.core.validators.MaxValueValidator(150),
                        ],
                        verbose_name="Weight:",
                    ),
                ),
                (
                    "sys_blood_pressure",
                    models.IntegerField(
                        help_text="in mm. format SYS, e.g. 120",
                        validators=[
                            django.core.validators.MinValueValidator(50),
                            django.core.validators.MaxValueValidator(220),
                        ],
                        verbose_name="Blood pressure: systolic",
                    ),
                ),
                (
                    "dia_blood_pressure",
                    models.IntegerField(
                        help_text="in Hg. format DIA, e.g. 80",
                        validators=[
                            django.core.validators.MinValueValidator(20),
                            django.core.validators.MaxValueValidator(150),
                        ],
                        verbose_name="Blood pressure: diastolic",
                    ),
                ),
                (
                    "heart_rate",
                    models.IntegerField(
                        help_text="BPM",
                        validators=[
                            django.core.validators.MinValueValidator(30),
                            django.core.validators.MaxValueValidator(200),
                        ],
                        verbose_name="Heart rate:",
                    ),
                ),
                (
                    "respiratory_rate",
                    models.IntegerField(
                        editable=False,
                        help_text="breaths/min",
                        null=True,
                        validators=[
                            django.core.validators.MinValueValidator(6),
                            django.core.validators.MaxValueValidator(50),
                        ],
                        verbose_name="Respiratory rate:",
                    ),
                ),
                (
                    "oxygen_saturation",
                    models.IntegerField(
                        editable=False,
                        help_text="%",
                        null=True,
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(999),
                        ],
                        verbose_name="Oxygen saturation:",
                    ),
                ),
                (
                    "temperature",
                    models.DecimalField(
                        decimal_places=1,
                        help_text="in degrees Celcius",
                        max_digits=3,
                        validators=[
                            django.core.validators.MinValueValidator(30),
                            django.core.validators.MaxValueValidator(45),
                        ],
                        verbose_name="Temperature:",
                    ),
                ),
                (
                    "is_heartbeat_regular",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")],
                        max_length=15,
                        verbose_name="Is the heart beat regular?",
                    ),
                ),
                (
                    "irregular_heartbeat",
                    models.TextField(
                        blank=True,
                        null=True,
                        verbose_name="If the heartbeat is NOT regular, please describe",
                    ),
                ),
                (
                    "waist_circumference",
                    models.DecimalField(
                        decimal_places=1,
                        help_text="in centimeters",
                        max_digits=5,
                        validators=[
                            django.core.validators.MinValueValidator(50.0),
                            django.core.validators.MaxValueValidator(175.0),
                        ],
                        verbose_name="Waist circumference",
                    ),
                ),
                (
                    "jaundice",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")],
                        max_length=15,
                        verbose_name="Jaundice",
                    ),
                ),
                (
                    "peripheral_oedema",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")],
                        max_length=15,
                        verbose_name="Presence of peripheral oedema",
                    ),
                ),
                (
                    "has_abdominal_tenderness",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")],
                        max_length=15,
                        verbose_name="Abdominal tenderness on palpation",
                    ),
                ),
                (
                    "abdominal_tenderness",
                    models.TextField(
                        blank=True,
                        null=True,
                        verbose_name="If YES, abdominal tenderness, please describe",
                    ),
                ),
                (
                    "has_enlarged_liver",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")],
                        max_length=15,
                        verbose_name="Enlarged liver on palpation",
                    ),
                ),
                ("history_date", models.DateTimeField()),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "site",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="sites.Site",
                    ),
                ),
                (
                    "subject_visit",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="meta_subject.SubjectVisit",
                    ),
                ),
            ],
            options={
                "verbose_name": "historical Patient History",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": "history_date",
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.AddIndex(
            model_name="physicalexam",
            index=models.Index(
                fields=["subject_visit", "site", "id"],
                name="meta_subjec_subject_7da1da_idx",
            ),
        ),
    ]

# Generated by Django 3.2.6 on 2021-09-23 21:27

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
        ("meta_subject", "0087_auto_20210922_2058"),
    ]

    operations = [
        migrations.AlterField(
            model_name="followupvitals",
            name="oxygen_saturation",
            field=models.IntegerField(
                blank=True,
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
                blank=True,
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
            name="oxygen_saturation",
            field=models.IntegerField(
                blank=True,
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
            model_name="historicalfollowupvitals",
            name="respiratory_rate",
            field=models.IntegerField(
                blank=True,
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
            model_name="historicalphysicalexam",
            name="oxygen_saturation",
            field=models.IntegerField(
                blank=True,
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
            model_name="historicalphysicalexam",
            name="respiratory_rate",
            field=models.IntegerField(
                blank=True,
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
            model_name="physicalexam",
            name="oxygen_saturation",
            field=models.IntegerField(
                blank=True,
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
            model_name="physicalexam",
            name="respiratory_rate",
            field=models.IntegerField(
                blank=True,
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
            name="HistoricalEq5d3l",
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
                    "consent_model",
                    models.CharField(editable=False, max_length=50, null=True),
                ),
                (
                    "consent_version",
                    models.CharField(editable=False, max_length=10, null=True),
                ),
                (
                    "mobility",
                    models.CharField(
                        choices=[
                            (
                                "no_problems_in_walking",
                                "I have no problems in walking about",
                            ),
                            (
                                "some_problems_in_walking",
                                "I have some problems in walking about",
                            ),
                            ("confined_to_bed", "I am confined to bed"),
                        ],
                        max_length=45,
                        verbose_name="Mobility",
                    ),
                ),
                (
                    "self_care",
                    models.CharField(
                        choices=[
                            (
                                "no_problems_with_self_care",
                                "I have no problems with self-care",
                            ),
                            (
                                "problems_washing_dressing_myself",
                                "I have some problems washing or dressing myself",
                            ),
                            (
                                "unable_to_wash_dress_myself",
                                "I am unable to wash or dress myself",
                            ),
                        ],
                        max_length=45,
                        verbose_name="SELF-CARE",
                    ),
                ),
                (
                    "usual_activities",
                    models.CharField(
                        choices=[
                            (
                                "no_problems_performing_usual_activities",
                                "I have no problems with performing my usual activities",
                            ),
                            (
                                "some_problems_performing_usual_activities",
                                "I have some problems with performing my usual activities",
                            ),
                            (
                                "unable_to_perform_usual_activities",
                                "I am unable to perform my usual activities",
                            ),
                        ],
                        help_text="Example. work, study, housework, family or leisure activities",
                        max_length=45,
                        verbose_name="USUAL ACTIVITIES",
                    ),
                ),
                (
                    "pain_discomfort",
                    models.CharField(
                        choices=[
                            ("no_pain_discomfort", "I have no pain or discomfort"),
                            (
                                "moderate_pain_discomfort",
                                "I have moderate pain or discomfort",
                            ),
                            (
                                "extreme_pain_discomfort",
                                "I have extreme pain or discomfort",
                            ),
                        ],
                        max_length=45,
                        verbose_name="PAIN/DISCOMFORT",
                    ),
                ),
                (
                    "anxiety_depression",
                    models.CharField(
                        choices=[
                            ("not_anxious_depressed", "I am not anxious or depressed"),
                            (
                                "moderately_anxious_depressed",
                                "I am moderately anxious or depressed",
                            ),
                            (
                                "extremely_anxious_depressed",
                                "I am extremely anxious or depressed",
                            ),
                        ],
                        max_length=45,
                        verbose_name="ANXIETY / DEPRESSION",
                    ),
                ),
                (
                    "health_today_score_slider",
                    models.CharField(
                        help_text="This scale is numbered from 0 to 100. 100 means the <U>best</U> health you can imagine0 means the <U>worst</U> health you can imagine.",
                        max_length=3,
                        verbose_name="Visual score for how your health is TODAY",
                    ),
                ),
                (
                    "health_today_score_confirmed",
                    models.IntegerField(
                        help_text="This scale is numbered from 0 to 100. 100 means the <U>best</U> health you can imagine0 means the <U>worst</U> health you can imagine.",
                        validators=[
                            django.core.validators.MinValueValidator(0),
                            django.core.validators.MaxValueValidator(100),
                        ],
                        verbose_name="<B><font color='orange'>Interviewer</font></B>: please confirm the number on the scale indicated from above.",
                    ),
                ),
                (
                    "crf_status",
                    models.CharField(
                        choices=[
                            ("INCOMPLETE", "Incomplete (some data pending)"),
                            ("COMPLETE", "Complete"),
                        ],
                        default="COMPLETE",
                        help_text="If some data is still pending, flag this CRF as incomplete",
                        max_length=25,
                        verbose_name="CRF status",
                    ),
                ),
                (
                    "crf_status_comments",
                    models.TextField(
                        blank=True,
                        help_text="for example, why some data is still pending",
                        null=True,
                        verbose_name="Any comments related to status of this CRF",
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
                        to="sites.site",
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
                        to="meta_subject.subjectvisit",
                    ),
                ),
            ],
            options={
                "verbose_name": "historical EuroQol EQ-5D-3L Instrument",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": "history_date",
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name="Eq5d3l",
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
                        help_text="If reporting today, use today's date/time, otherwise use the date/time this information was reported.",
                        validators=[
                            edc_protocol.validators.datetime_not_before_study_start,
                            edc_model.validators.date.datetime_not_future,
                        ],
                        verbose_name="Report Date",
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
                    "mobility",
                    models.CharField(
                        choices=[
                            (
                                "no_problems_in_walking",
                                "I have no problems in walking about",
                            ),
                            (
                                "some_problems_in_walking",
                                "I have some problems in walking about",
                            ),
                            ("confined_to_bed", "I am confined to bed"),
                        ],
                        max_length=45,
                        verbose_name="Mobility",
                    ),
                ),
                (
                    "self_care",
                    models.CharField(
                        choices=[
                            (
                                "no_problems_with_self_care",
                                "I have no problems with self-care",
                            ),
                            (
                                "problems_washing_dressing_myself",
                                "I have some problems washing or dressing myself",
                            ),
                            (
                                "unable_to_wash_dress_myself",
                                "I am unable to wash or dress myself",
                            ),
                        ],
                        max_length=45,
                        verbose_name="SELF-CARE",
                    ),
                ),
                (
                    "usual_activities",
                    models.CharField(
                        choices=[
                            (
                                "no_problems_performing_usual_activities",
                                "I have no problems with performing my usual activities",
                            ),
                            (
                                "some_problems_performing_usual_activities",
                                "I have some problems with performing my usual activities",
                            ),
                            (
                                "unable_to_perform_usual_activities",
                                "I am unable to perform my usual activities",
                            ),
                        ],
                        help_text="Example. work, study, housework, family or leisure activities",
                        max_length=45,
                        verbose_name="USUAL ACTIVITIES",
                    ),
                ),
                (
                    "pain_discomfort",
                    models.CharField(
                        choices=[
                            ("no_pain_discomfort", "I have no pain or discomfort"),
                            (
                                "moderate_pain_discomfort",
                                "I have moderate pain or discomfort",
                            ),
                            (
                                "extreme_pain_discomfort",
                                "I have extreme pain or discomfort",
                            ),
                        ],
                        max_length=45,
                        verbose_name="PAIN/DISCOMFORT",
                    ),
                ),
                (
                    "anxiety_depression",
                    models.CharField(
                        choices=[
                            ("not_anxious_depressed", "I am not anxious or depressed"),
                            (
                                "moderately_anxious_depressed",
                                "I am moderately anxious or depressed",
                            ),
                            (
                                "extremely_anxious_depressed",
                                "I am extremely anxious or depressed",
                            ),
                        ],
                        max_length=45,
                        verbose_name="ANXIETY / DEPRESSION",
                    ),
                ),
                (
                    "health_today_score_slider",
                    models.CharField(
                        help_text="This scale is numbered from 0 to 100. 100 means the <U>best</U> health you can imagine0 means the <U>worst</U> health you can imagine.",
                        max_length=3,
                        verbose_name="Visual score for how your health is TODAY",
                    ),
                ),
                (
                    "health_today_score_confirmed",
                    models.IntegerField(
                        help_text="This scale is numbered from 0 to 100. 100 means the <U>best</U> health you can imagine0 means the <U>worst</U> health you can imagine.",
                        validators=[
                            django.core.validators.MinValueValidator(0),
                            django.core.validators.MaxValueValidator(100),
                        ],
                        verbose_name="<B><font color='orange'>Interviewer</font></B>: please confirm the number on the scale indicated from above.",
                    ),
                ),
                (
                    "crf_status",
                    models.CharField(
                        choices=[
                            ("INCOMPLETE", "Incomplete (some data pending)"),
                            ("COMPLETE", "Complete"),
                        ],
                        default="COMPLETE",
                        help_text="If some data is still pending, flag this CRF as incomplete",
                        max_length=25,
                        verbose_name="CRF status",
                    ),
                ),
                (
                    "crf_status_comments",
                    models.TextField(
                        blank=True,
                        help_text="for example, why some data is still pending",
                        null=True,
                        verbose_name="Any comments related to status of this CRF",
                    ),
                ),
                (
                    "site",
                    models.ForeignKey(
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="+",
                        to="sites.site",
                    ),
                ),
                (
                    "subject_visit",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="meta_subject.subjectvisit",
                    ),
                ),
            ],
            options={
                "verbose_name": "EuroQol EQ-5D-3L Instrument",
                "verbose_name_plural": "EuroQol EQ-5D-3L Instrument",
                "ordering": ("-modified", "-created"),
                "get_latest_by": "modified",
                "abstract": False,
                "default_permissions": (
                    "add",
                    "change",
                    "delete",
                    "view",
                    "export",
                    "import",
                ),
            },
            managers=[
                ("on_site", django.contrib.sites.managers.CurrentSiteManager()),
                ("objects", edc_visit_tracking.managers.CrfModelManager()),
            ],
        ),
    ]

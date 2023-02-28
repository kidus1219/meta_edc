# Generated by Django 3.2.11 on 2022-05-12 15:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("meta_subject", "0109_auto_20220415_1758"),
    ]

    operations = [
        migrations.AddField(
            model_name="historicalsubjectvisit",
            name="document_status",
            field=models.CharField(
                choices=[
                    ("INCOMPLETE", "Incomplete (some data pending)"),
                    ("COMPLETE", "Complete"),
                ],
                default="COMPLETE",
                help_text="If some data is still pending, flag as incomplete",
                max_length=25,
                verbose_name="Document status",
            ),
        ),
        migrations.AddField(
            model_name="subjectvisit",
            name="document_status",
            field=models.CharField(
                choices=[
                    ("INCOMPLETE", "Incomplete (some data pending)"),
                    ("COMPLETE", "Complete"),
                ],
                default="COMPLETE",
                help_text="If some data is still pending, flag as incomplete",
                max_length=25,
                verbose_name="Document status",
            ),
        ),
        migrations.AlterField(
            model_name="historicalsubjectvisit",
            name="survival_status",
            field=models.CharField(
                choices=[
                    ("alive", "Alive"),
                    ("dead", "Deceased"),
                    ("unknown", "Unknown"),
                    ("N/A", "Not applicable (if missed)"),
                ],
                default="alive",
                help_text="If YES, submit Death report",
                max_length=10,
                null=True,
                verbose_name="Participant's survival status",
            ),
        ),
        migrations.AlterField(
            model_name="subjectvisit",
            name="survival_status",
            field=models.CharField(
                choices=[
                    ("alive", "Alive"),
                    ("dead", "Deceased"),
                    ("unknown", "Unknown"),
                    ("N/A", "Not applicable (if missed)"),
                ],
                default="alive",
                help_text="If YES, submit Death report",
                max_length=10,
                null=True,
                verbose_name="Participant's survival status",
            ),
        ),
    ]

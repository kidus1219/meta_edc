# Generated by Django 4.0.5 on 2022-07-03 19:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("meta_prn", "0041_endofstudy_transfer_date_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="endofstudy",
            name="investigator_decision",
        ),
        migrations.RemoveField(
            model_name="historicalendofstudy",
            name="investigator_decision",
        ),
        migrations.AddField(
            model_name="endofstudy",
            name="clinical_withdrawal_investigator_decision",
            field=models.TextField(
                blank=True,
                max_length=500,
                null=True,
                verbose_name="If withdrawl was an 'investigator decision', please explain ...",
            ),
        ),
        migrations.AddField(
            model_name="historicalendofstudy",
            name="clinical_withdrawal_investigator_decision",
            field=models.TextField(
                blank=True,
                max_length=500,
                null=True,
                verbose_name="If withdrawl was an 'investigator decision', please explain ...",
            ),
        ),
        migrations.AlterField(
            model_name="endofstudy",
            name="clinical_withdrawal_reason",
            field=models.CharField(
                choices=[
                    ("kidney_disease", "Development of chronic kidney disease"),
                    ("liver_disease", "Development of chronic liver disease"),
                    (
                        "intercurrent_illness",
                        "Intercurrent illness which prevents further treatment",
                    ),
                    ("investigator_decision", "Investigator decision (specify below)"),
                    (
                        "OTHER",
                        "Other condition that justifies the discontinuation of treatment in the clinician’s opinion (specify below)",
                    ),
                    ("N/A", "Not applicable"),
                ],
                default="N/A",
                max_length=25,
                verbose_name="If the patient was withdrawn on CLINICAL grounds, please specify PRIMARY reason",
            ),
        ),
        migrations.AlterField(
            model_name="endofstudy",
            name="clinical_withdrawal_reason_other",
            field=models.TextField(
                blank=True,
                max_length=500,
                null=True,
                verbose_name="If withdrawn for 'other' condition, please explain",
            ),
        ),
        migrations.AlterField(
            model_name="endofstudy",
            name="toxicity_withdrawal_reason",
            field=models.CharField(
                choices=[
                    ("lactic_acidosis", "Development of lactic acidosis or hyperlactatemia"),
                    ("hepatomegaly", "Development of hepatomegaly with steatosis"),
                    ("OTHER", "Other toxicity (specify below)"),
                    ("N/A", "Not applicable"),
                ],
                default="N/A",
                max_length=25,
                verbose_name=" If the patient experienced an unacceptable toxicity', please explain",
            ),
        ),
        migrations.AlterField(
            model_name="endofstudy",
            name="toxicity_withdrawal_reason_other",
            field=models.TextField(
                blank=True,
                max_length=500,
                null=True,
                verbose_name="If 'other toxicity', please specify ...",
            ),
        ),
        migrations.AlterField(
            model_name="historicalendofstudy",
            name="clinical_withdrawal_reason",
            field=models.CharField(
                choices=[
                    ("kidney_disease", "Development of chronic kidney disease"),
                    ("liver_disease", "Development of chronic liver disease"),
                    (
                        "intercurrent_illness",
                        "Intercurrent illness which prevents further treatment",
                    ),
                    ("investigator_decision", "Investigator decision (specify below)"),
                    (
                        "OTHER",
                        "Other condition that justifies the discontinuation of treatment in the clinician’s opinion (specify below)",
                    ),
                    ("N/A", "Not applicable"),
                ],
                default="N/A",
                max_length=25,
                verbose_name="If the patient was withdrawn on CLINICAL grounds, please specify PRIMARY reason",
            ),
        ),
        migrations.AlterField(
            model_name="historicalendofstudy",
            name="clinical_withdrawal_reason_other",
            field=models.TextField(
                blank=True,
                max_length=500,
                null=True,
                verbose_name="If withdrawn for 'other' condition, please explain",
            ),
        ),
        migrations.AlterField(
            model_name="historicalendofstudy",
            name="toxicity_withdrawal_reason",
            field=models.CharField(
                choices=[
                    ("lactic_acidosis", "Development of lactic acidosis or hyperlactatemia"),
                    ("hepatomegaly", "Development of hepatomegaly with steatosis"),
                    ("OTHER", "Other toxicity (specify below)"),
                    ("N/A", "Not applicable"),
                ],
                default="N/A",
                max_length=25,
                verbose_name=" If the patient experienced an unacceptable toxicity', please explain",
            ),
        ),
        migrations.AlterField(
            model_name="historicalendofstudy",
            name="toxicity_withdrawal_reason_other",
            field=models.TextField(
                blank=True,
                max_length=500,
                null=True,
                verbose_name="If 'other toxicity', please specify ...",
            ),
        ),
    ]

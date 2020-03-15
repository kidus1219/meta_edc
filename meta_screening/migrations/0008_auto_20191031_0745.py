# Generated by Django 2.2.6 on 2019-10-31 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("meta_screening", "0007_auto_20191024_1000")]

    operations = [
        migrations.AlterField(
            model_name="historicalscreeningpartone",
            name="pregnant",
            field=models.CharField(
                choices=[
                    ("Yes", "Yes"),
                    ("No", "No"),
                    (
                        "N/A",
                        "Not Applicable: e.g. mentruating, post menopausal, not female",
                    ),
                ],
                max_length=15,
                verbose_name="Is the patient pregnant?",
            ),
        ),
        migrations.AlterField(
            model_name="historicalscreeningpartone",
            name="urine_bhcg_performed",
            field=models.CharField(
                choices=[
                    ("Yes", "Yes"),
                    ("No", "No"),
                    (
                        "N/A",
                        "Not Applicable: e.g. mentruating, post menopausal, not female",
                    ),
                ],
                default="N/A",
                help_text="(Pregnancy test)",
                max_length=15,
                verbose_name="Was a Urine or serum βhCG performed?",
            ),
        ),
        migrations.AlterField(
            model_name="historicalscreeningpartthree",
            name="pregnant",
            field=models.CharField(
                choices=[
                    ("Yes", "Yes"),
                    ("No", "No"),
                    (
                        "N/A",
                        "Not Applicable: e.g. mentruating, post menopausal, not female",
                    ),
                ],
                max_length=15,
                verbose_name="Is the patient pregnant?",
            ),
        ),
        migrations.AlterField(
            model_name="historicalscreeningpartthree",
            name="urine_bhcg_performed",
            field=models.CharField(
                choices=[
                    ("Yes", "Yes"),
                    ("No", "No"),
                    (
                        "N/A",
                        "Not Applicable: e.g. mentruating, post menopausal, not female",
                    ),
                ],
                default="N/A",
                help_text="(Pregnancy test)",
                max_length=15,
                verbose_name="Was a Urine or serum βhCG performed?",
            ),
        ),
        migrations.AlterField(
            model_name="historicalscreeningparttwo",
            name="pregnant",
            field=models.CharField(
                choices=[
                    ("Yes", "Yes"),
                    ("No", "No"),
                    (
                        "N/A",
                        "Not Applicable: e.g. mentruating, post menopausal, not female",
                    ),
                ],
                max_length=15,
                verbose_name="Is the patient pregnant?",
            ),
        ),
        migrations.AlterField(
            model_name="historicalscreeningparttwo",
            name="urine_bhcg_performed",
            field=models.CharField(
                choices=[
                    ("Yes", "Yes"),
                    ("No", "No"),
                    (
                        "N/A",
                        "Not Applicable: e.g. mentruating, post menopausal, not female",
                    ),
                ],
                default="N/A",
                help_text="(Pregnancy test)",
                max_length=15,
                verbose_name="Was a Urine or serum βhCG performed?",
            ),
        ),
        migrations.AlterField(
            model_name="historicalsubjectscreening",
            name="pregnant",
            field=models.CharField(
                choices=[
                    ("Yes", "Yes"),
                    ("No", "No"),
                    (
                        "N/A",
                        "Not Applicable: e.g. mentruating, post menopausal, not female",
                    ),
                ],
                max_length=15,
                verbose_name="Is the patient pregnant?",
            ),
        ),
        migrations.AlterField(
            model_name="historicalsubjectscreening",
            name="urine_bhcg_performed",
            field=models.CharField(
                choices=[
                    ("Yes", "Yes"),
                    ("No", "No"),
                    (
                        "N/A",
                        "Not Applicable: e.g. mentruating, post menopausal, not female",
                    ),
                ],
                default="N/A",
                help_text="(Pregnancy test)",
                max_length=15,
                verbose_name="Was a Urine or serum βhCG performed?",
            ),
        ),
        migrations.AlterField(
            model_name="subjectscreening",
            name="pregnant",
            field=models.CharField(
                choices=[
                    ("Yes", "Yes"),
                    ("No", "No"),
                    (
                        "N/A",
                        "Not Applicable: e.g. mentruating, post menopausal, not female",
                    ),
                ],
                max_length=15,
                verbose_name="Is the patient pregnant?",
            ),
        ),
        migrations.AlterField(
            model_name="subjectscreening",
            name="urine_bhcg_performed",
            field=models.CharField(
                choices=[
                    ("Yes", "Yes"),
                    ("No", "No"),
                    (
                        "N/A",
                        "Not Applicable: e.g. mentruating, post menopausal, not female",
                    ),
                ],
                default="N/A",
                help_text="(Pregnancy test)",
                max_length=15,
                verbose_name="Was a Urine or serum βhCG performed?",
            ),
        ),
    ]

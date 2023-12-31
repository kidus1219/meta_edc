# Generated by Django 4.0.5 on 2022-06-28 19:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("meta_screening", "0051_alter_historicalscreeningpartone_advised_to_fast_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="historicalscreeningpartone",
            name="p3_ltfu",
            field=models.CharField(
                choices=[
                    ("Yes", "Yes"),
                    ("PENDING", "Decision pending"),
                    ("N/A", "Not applicable"),
                ],
                default="N/A",
                help_text="Only applicable if the patient missed the appointment for the second stage of screening (P3), several attempts have been made to contact the patient, and the patient has not started P3. See above",
                max_length=15,
                verbose_name="Consider the patient 'lost to screening' for now?",
            ),
        ),
        migrations.AlterField(
            model_name="historicalscreeningpartthree",
            name="p3_ltfu",
            field=models.CharField(
                choices=[
                    ("Yes", "Yes"),
                    ("PENDING", "Decision pending"),
                    ("N/A", "Not applicable"),
                ],
                default="N/A",
                help_text="Only applicable if the patient missed the appointment for the second stage of screening (P3), several attempts have been made to contact the patient, and the patient has not started P3. See above",
                max_length=15,
                verbose_name="Consider the patient 'lost to screening' for now?",
            ),
        ),
        migrations.AlterField(
            model_name="historicalscreeningparttwo",
            name="p3_ltfu",
            field=models.CharField(
                choices=[
                    ("Yes", "Yes"),
                    ("PENDING", "Decision pending"),
                    ("N/A", "Not applicable"),
                ],
                default="N/A",
                help_text="Only applicable if the patient missed the appointment for the second stage of screening (P3), several attempts have been made to contact the patient, and the patient has not started P3. See above",
                max_length=15,
                verbose_name="Consider the patient 'lost to screening' for now?",
            ),
        ),
        migrations.AlterField(
            model_name="historicalsubjectscreening",
            name="p3_ltfu",
            field=models.CharField(
                choices=[
                    ("Yes", "Yes"),
                    ("PENDING", "Decision pending"),
                    ("N/A", "Not applicable"),
                ],
                default="N/A",
                help_text="Only applicable if the patient missed the appointment for the second stage of screening (P3), several attempts have been made to contact the patient, and the patient has not started P3. See above",
                max_length=15,
                verbose_name="Consider the patient 'lost to screening' for now?",
            ),
        ),
        migrations.AlterField(
            model_name="subjectscreening",
            name="p3_ltfu",
            field=models.CharField(
                choices=[
                    ("Yes", "Yes"),
                    ("PENDING", "Decision pending"),
                    ("N/A", "Not applicable"),
                ],
                default="N/A",
                help_text="Only applicable if the patient missed the appointment for the second stage of screening (P3), several attempts have been made to contact the patient, and the patient has not started P3. See above",
                max_length=15,
                verbose_name="Consider the patient 'lost to screening' for now?",
            ),
        ),
    ]

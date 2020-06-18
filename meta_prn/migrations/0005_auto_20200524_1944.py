# Generated by Django 3.0.6 on 2020-05-24 16:44

from django.db import migrations, models
import edc_model.models.fields.other_charfield
import edc_model.validators.date


class Migration(migrations.Migration):

    dependencies = [
        ("meta_prn", "0004_auto_20200403_0332"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="historicallosstofollowup", name="phone_attempts",
        ),
        migrations.RemoveField(model_name="losstofollowup", name="phone_attempts",),
        migrations.AddField(
            model_name="endofstudy",
            name="ltfu_date",
            field=models.DateField(
                blank=True,
                null=True,
                validators=[edc_model.validators.date.date_not_future],
                verbose_name="Date lost to followup, if applicable",
            ),
        ),
        migrations.AddField(
            model_name="historicalendofstudy",
            name="ltfu_date",
            field=models.DateField(
                blank=True,
                null=True,
                validators=[edc_model.validators.date.date_not_future],
                verbose_name="Date lost to followup, if applicable",
            ),
        ),
        migrations.AddField(
            model_name="historicallosstofollowup",
            name="last_missed_visit_datetime",
            field=models.DateField(
                null=True, verbose_name="Date of last missed visit report submitted"
            ),
        ),
        migrations.AddField(
            model_name="historicallosstofollowup",
            name="loss_category_other",
            field=edc_model.models.fields.other_charfield.OtherCharField(
                blank=True,
                max_length=35,
                null=True,
                verbose_name="If other, please specify ...",
            ),
        ),
        migrations.AddField(
            model_name="historicallosstofollowup",
            name="number_consecutive_missed_visits",
            field=models.DateField(
                null=True, verbose_name="Number of consecutive visits missed"
            ),
        ),
        migrations.AddField(
            model_name="losstofollowup",
            name="last_missed_visit_datetime",
            field=models.DateField(
                null=True, verbose_name="Date of last missed visit report submitted"
            ),
        ),
        migrations.AddField(
            model_name="losstofollowup",
            name="loss_category_other",
            field=edc_model.models.fields.other_charfield.OtherCharField(
                blank=True,
                max_length=35,
                null=True,
                verbose_name="If other, please specify ...",
            ),
        ),
        migrations.AddField(
            model_name="losstofollowup",
            name="number_consecutive_missed_visits",
            field=models.DateField(
                null=True, verbose_name="Number of consecutive visits missed"
            ),
        ),
        migrations.AlterField(
            model_name="historicallosstofollowup",
            name="loss_category",
            field=models.CharField(
                choices=[
                    ("unknown_address", "Changed to an unknown address"),
                    ("never_returned", "Did not return despite reminders"),
                    ("bad_contact_details", "Inaccurate contact details"),
                    ("OTHER", "Other, please specify ..."),
                ],
                max_length=25,
                verbose_name="Category of loss to follow up",
            ),
        ),
        migrations.AlterField(
            model_name="losstofollowup",
            name="loss_category",
            field=models.CharField(
                choices=[
                    ("unknown_address", "Changed to an unknown address"),
                    ("never_returned", "Did not return despite reminders"),
                    ("bad_contact_details", "Inaccurate contact details"),
                    ("OTHER", "Other, please specify ..."),
                ],
                max_length=25,
                verbose_name="Category of loss to follow up",
            ),
        ),
    ]

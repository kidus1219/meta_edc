# Generated by Django 3.2.13 on 2022-09-07 12:05
from django.core.exceptions import ObjectDoesNotExist
from django.db import migrations
from edc_appointment.utils import get_next_appointment


def update_refill_end_datetimes(apps, schema_editor):
    rx_model_cls = apps.get_model("edc_pharmacy.rx")
    rx_refill_model_cls = apps.get_model("edc_pharmacy.rxrefill")
    appointment_model_cls = apps.get_model("edc_appointment.appointment")
    subject_visit_model_cls = apps.get_model("meta_subject.subjectvisit")
    model_cls = apps.get_model("meta_subject.studymedication")
    for obj in model_cls._default_manager.filter(refill_end_datetime__isnull=True).order_by(
        "refill_start_datetime"
    ):
        subject_visit = subject_visit_model_cls._default_manager.get(id=obj.subject_visit_id)
        appointment = appointment_model_cls._default_manager.get(
            id=subject_visit.appointment_id
        )
        try:
            rx_refill = rx_refill_model_cls._default_manager.get(
                refill_start_datetime=obj.refill_start_datetime,
                rx__subject_identifier=appointment.subject_identifier,
            )
        except ObjectDoesNotExist:
            rx_refill = None
        try:
            obj.refill_end_datetime = get_next_appointment(
                appointment, include_interim=True
            ).appt_datetime
        except AttributeError:
            print(f"Unable to update. No next appt. Got {obj}.")
        else:
            obj.save_base(update_fields=["refill_end_datetime"])
            if rx_refill:
                rx_refill.refill_end_datetime = obj.refill_end_datetime
                rx_refill.save_base(update_fields=["refill_end_datetime"])


class Migration(migrations.Migration):
    dependencies = [
        ("meta_subject", "0146_auto_20220907_0207"),
    ]

    operations = [migrations.RunPython(update_refill_end_datetimes)]

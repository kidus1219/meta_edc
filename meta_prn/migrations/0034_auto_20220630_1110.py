# Generated by Django 4.0.5 on 2022-06-30 08:10
from django.core.exceptions import ObjectDoesNotExist
from django.db import migrations
from django.db.models.signals import post_save, pre_save
from edc_constants.constants import HIGH
from edc_protocol_incident.constants import PROTOCOL_INCIDENT_ACTION
from edc_utils import DisableSignals

from meta_prn.constants import PROTOCOL_DEVIATION_VIOLATION_ACTION


def update_for_protocol_incident(apps, schema_editor):
    action_item_model_cls = apps.get_model("edc_action_item.actionitem")
    action_type_model_cls = apps.get_model("edc_action_item.actiontype")
    crf_metadata_model_cls = apps.get_model("edc_metadata.crfmetadata")

    with DisableSignals(disabled_signals=[pre_save, post_save]):
        # update crf metadata if there is any
        crf_metadata_model_cls.objects.filter(
            model="meta_prn.protocoldeviationviolation"
        ).update(model="meta_prn.protocolincident")

        # update action type
        try:
            action_type = action_type_model_cls.objects.get(name=PROTOCOL_INCIDENT_ACTION)
        except ObjectDoesNotExist:
            action_type = action_type_model_cls.objects.create(
                name=PROTOCOL_INCIDENT_ACTION,
                display_name=PROTOCOL_INCIDENT_ACTION,
                reference_model="meta_prn.protocolincident",
                priority=HIGH,
                show_on_dashboard=True,
                show_link_to_changelist=True,
            )
        action_item_model_cls.objects.filter(
            action_type__name=PROTOCOL_DEVIATION_VIOLATION_ACTION
        ).update(action_type=action_type)

        # update crf metadata if there is any
        action_item_model_cls.objects.filter(
            reference_model="meta_prn.protocoldeviationviolation"
        ).update(reference_model="meta_prn.protocolincident")


class Migration(migrations.Migration):

    dependencies = [
        ("meta_prn", "0033_remove_historicalegfrnotification_action_item_and_more"),
    ]

    operations = [migrations.RunPython(update_for_protocol_incident)]

from edc_action_item.models import ActionModelMixin
from edc_identifier.model_mixins import TrackingModelMixin
from edc_model.models import BaseUuidModel
from edc_visit_schedule.model_mixins import OffScheduleModelMixin

from meta_prn.constants import (
    OFFSCHEDULE_ACTION,
    OFFSCHEDULE_POSTNATAL_ACTION,
    OFFSCHEDULE_PREGNANCY_ACTION,
)


class OffSchedule(
    ActionModelMixin, TrackingModelMixin, OffScheduleModelMixin, BaseUuidModel
):

    action_name = OFFSCHEDULE_ACTION

    tracking_identifier_prefix = "OX"

    class Meta(OffScheduleModelMixin.Meta):
        pass


class OffSchedulePregnancy(
    ActionModelMixin, TrackingModelMixin, OffScheduleModelMixin, BaseUuidModel
):
    action_name = OFFSCHEDULE_PREGNANCY_ACTION

    tracking_identifier_prefix = "OP"

    class Meta(OffScheduleModelMixin.Meta):
        pass


class OffSchedulePostnatal(
    ActionModelMixin, TrackingModelMixin, OffScheduleModelMixin, BaseUuidModel
):
    action_name = OFFSCHEDULE_POSTNATAL_ACTION

    tracking_identifier_prefix = "ON"

    class Meta(OffScheduleModelMixin.Meta):
        pass

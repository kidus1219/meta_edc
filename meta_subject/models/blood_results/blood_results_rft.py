from django.db import models
from edc_crf.crf_with_action_model_mixin import CrfWithActionModelMixin
from edc_egfr.model_mixins import EgfrDropModelMixin, EgfrModelMixin
from edc_lab.model_mixins import CrfWithRequisitionModelMixin
from edc_lab_panel.panels import rft_panel
from edc_lab_results import BLOOD_RESULTS_RFT_ACTION
from edc_lab_results.model_mixins import (
    BloodResultsModelMixin,
    CreatinineModelMixin,
    UreaModelMixin,
    UricAcidModelMixin,
)
from edc_model import models as edc_models


class BloodResultsRft(
    CrfWithActionModelMixin,
    CreatinineModelMixin,
    EgfrModelMixin,
    EgfrDropModelMixin,
    UreaModelMixin,
    UricAcidModelMixin,
    CrfWithRequisitionModelMixin,
    BloodResultsModelMixin,
    edc_models.BaseUuidModel,
):
    action_name = BLOOD_RESULTS_RFT_ACTION
    tracking_identifier_prefix = "RF"
    lab_panel = rft_panel
    egfr_formula_name = "ckd-epi"

    old_egfr_value = models.DecimalField(
        decimal_places=4,
        max_digits=8,
        null=True,
        editable=False,
        help_text="incorrect ckd-epi calculation (w/ 1.150 as ethnicity factor)",
    )

    old_egfr_drop_value = models.DecimalField(
        decimal_places=4,
        max_digits=10,
        null=True,
        editable=False,
        help_text="incorrect ckd-epi calculation (w/ 1.150 as ethnicity factor)",
    )

    class Meta(CrfWithActionModelMixin.Meta, edc_models.BaseUuidModel.Meta):
        verbose_name = "Blood Result: RFT"
        verbose_name_plural = "Blood Results: RFT"

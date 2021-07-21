from django.db import models
from edc_constants.choices import YES_NO
from edc_model import models as edc_models

from meta_lists.models import AbnormalFootAppearanceObservations

from ..choices import (
    ANKLE_REFLEX_CHOICES,
    MONOFILAMENT_CHOICES,
    ULCERATION_CHOICES,
    VIBRATION_PERCEPTION_CHOICES,
)
from .model_mixins import CrfModelMixin


class Mnsi(
    CrfModelMixin,
    edc_models.BaseUuidModel,
):

    """Neuropathy screening tool.

    Uses Michigan Neuropathy Screening Instrument (MNSI), see:
        https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3641573/ (omits monofilament testing)
        https://medicine.umich.edu/sites/default/files/downloads/MNSI_howto.pdf

    """

    numb_legs_feet = models.CharField(
        verbose_name="Are your legs and/or feet numb?",
        max_length=15,
        choices=YES_NO,
    )

    burning_pain_legs_feet = models.CharField(
        verbose_name="Do you ever have any burning pain in your legs and/or feet?",
        max_length=15,
        choices=YES_NO,
    )

    feet_sensitive_touch = models.CharField(
        verbose_name="Are your feet too sensitive to touch?",
        max_length=15,
        choices=YES_NO,
    )

    muscle_cramps_legs_feet = models.CharField(
        verbose_name="Do you get muscle cramps in your legs and/or feet?",
        max_length=15,
        choices=YES_NO,
    )

    prickling_feelings_legs_feet = models.CharField(
        verbose_name="Do you ever have any prickling feelings in your legs or feet?",
        max_length=15,
        choices=YES_NO,
    )

    covers_touch_skin_painful = models.CharField(
        verbose_name="Does it hurt when the bed covers touch your skin?",
        max_length=15,
        choices=YES_NO,
    )

    differentiate_hot_cold_water = models.CharField(
        verbose_name="When you get into the tub or shower, are you able to tell the hot water from the cold water?",
        max_length=15,
        choices=YES_NO,
    )

    open_sore_foot_history = models.CharField(
        verbose_name="Have you ever had an open sore on your foot?",
        max_length=15,
        choices=YES_NO,
    )

    diabetic_neuropathy = models.CharField(
        verbose_name="Has your doctor ever told you that you have diabetic neuropathy?",
        max_length=15,
        choices=YES_NO,
    )

    feel_weak = models.CharField(
        verbose_name="Do you feel weak all over most of the time?",
        max_length=15,
        choices=YES_NO,
    )

    symptoms_worse_night = models.CharField(
        verbose_name="Are your symptoms worse at night?",
        max_length=15,
        choices=YES_NO,
    )

    legs_hurt_when_walk = models.CharField(
        verbose_name="Do your legs hurt when you walk?",
        max_length=15,
        choices=YES_NO,
    )

    sense_feet_when_walk = models.CharField(
        verbose_name="Are you able to sense your feet when you walk?",
        max_length=15,
        choices=YES_NO,
    )

    skin_cracks_open_feet = models.CharField(
        verbose_name="Is the skin on your feet so dry that it cracks open?",
        max_length=15,
        choices=YES_NO,
    )

    amputation = models.CharField(
        verbose_name="Have you ever had an amputation?",
        max_length=15,
        choices=YES_NO,
    )

    normal_appearance_right_foot = models.CharField(
        verbose_name="Does RIGHT foot appear normal?",
        max_length=15,
        choices=YES_NO,
    )

    abnormal_appearance_observations_right_foot = models.ManyToManyField(
        AbnormalFootAppearanceObservations,
        related_name="abnormal_appearance_observations_right_foot",
        verbose_name="If NO, check all that apply to RIGHT foot?",
        blank=True,
    )

    abnormal_appearance_observations_right_foot_other = edc_models.OtherCharField(
        verbose_name="If other abnormality observed on RIGHT foot, please specify ..."
    )

    ulceration_right_foot = models.CharField(
        verbose_name="Ulceration, RIGHT foot?",
        max_length=15,
        choices=ULCERATION_CHOICES,
    )

    ankle_reflexes_right_foot = models.CharField(
        verbose_name="Ankle reflexes, RIGHT foot?",
        max_length=25,
        choices=ANKLE_REFLEX_CHOICES,
    )

    vibration_perception_right_toe = models.CharField(
        verbose_name="Vibration perception at great toe, RIGHT foot?",
        max_length=15,
        choices=VIBRATION_PERCEPTION_CHOICES,
    )

    monofilament_right_foot = models.CharField(
        verbose_name="Monofilament, RIGHT foot?",
        max_length=15,
        choices=MONOFILAMENT_CHOICES,
    )

    normal_appearance_left_foot = models.CharField(
        verbose_name="Does LEFT foot appear normal?",
        max_length=15,
        choices=YES_NO,
    )

    abnormal_appearance_observations_left_foot = models.ManyToManyField(
        AbnormalFootAppearanceObservations,
        related_name="abnormal_appearance_observations_left_foot",
        verbose_name="If NO, check all that apply to LEFT foot?",
        blank=True,
    )

    abnormal_appearance_observations_left_foot_other = edc_models.OtherCharField(
        verbose_name="If other abnormality observed on LEFT foot, please specify ..."
    )

    ulceration_left_foot = models.CharField(
        verbose_name="Ulceration, LEFT foot?",
        max_length=15,
        choices=ULCERATION_CHOICES,
    )

    ankle_reflexes_left_foot = models.CharField(
        verbose_name="Ankle reflexes, LEFT foot?",
        max_length=25,
        choices=ANKLE_REFLEX_CHOICES,
    )

    vibration_perception_left_toe = models.CharField(
        verbose_name="Vibration perception at great toe, LEFT foot?",
        max_length=15,
        choices=VIBRATION_PERCEPTION_CHOICES,
    )

    monofilament_left_foot = models.CharField(
        verbose_name="Monofilament, LEFT foot?",
        max_length=15,
        choices=MONOFILAMENT_CHOICES,
    )

    class Meta(CrfModelMixin.Meta, edc_models.BaseUuidModel.Meta):
        verbose_name = "Michigan Neuropathy Screening Instrument (MNSI)"
        verbose_name_plural = "Michigan Neuropathy Screening Instrument (MNSI)"

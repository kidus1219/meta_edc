from django.contrib import admin
from django_audit_fields.admin import audit_fieldset_tuple
from edc_form_label.form_label_modeladmin_mixin import FormLabelModelAdminMixin
from edc_model_admin import SimpleHistoryAdmin


from ..admin_site import meta_subject_admin
from ..forms import MissedVisitForm
from ..models import MissedVisit
from .modeladmin import CrfModelAdminMixin


@admin.register(MissedVisit, site=meta_subject_admin)
class MissedVisitAdmin(
    CrfModelAdminMixin, FormLabelModelAdminMixin, SimpleHistoryAdmin
):

    form = MissedVisitForm

    fieldsets = (
        (None, {"fields": ("subject_visit", "report_datetime")}),
        (
            "Contact History",
            {
                "fields": (
                    "survival_status",
                    "contact_attempted",
                    "contact_made",
                    "contact_attempts_count",
                    "contact_attempts_explained",
                    "contact_last_date",
                    "missed_reasons",
                    "missed_reasons_other",
                    "comment",
                ),
            },
        ),
        audit_fieldset_tuple,
    )

    filter_horizontal = ("missed_reasons",)

    radio_fields = {
        "survival_status": admin.VERTICAL,
        "contact_attempted": admin.VERTICAL,
        "contact_made": admin.VERTICAL,
    }

from copy import deepcopy
from operator import itemgetter

row_sep = f"+{'-' * 32}+{'-' * 32}+"
justify = 30


def print_table(data, module_name):
    rows = {}
    for row in data:
        model_name = row["model_name"]
        try:
            rows[model_name].append([row["old_name"], row["new_name"]])
        except KeyError:
            rows[model_name] = []
            rows[model_name].append([row["old_name"], row["new_name"]])
    for model_name in rows:
        rows[model_name] = sorted(rows[model_name], key=itemgetter(0))

    for table_name, field_pair in rows.items():
        print("")
        print(f"Table: {module_name}_{table_name}")
        print(row_sep)
        print(f"| {'OLD NAME'.ljust(justify)} | {'NEW NAME'.ljust(justify)} |")
        print(row_sep)
        for old_name, new_name in field_pair:
            print(f"| {old_name.ljust(justify)} | {new_name.ljust(justify)} |")
            print(row_sep)


def fields_summary(data, fields=None):
    fields = fields or {}
    for row in data:
        field_name = row["old_name"]
        try:
            fields[field_name].append(row["new_name"])
        except KeyError:
            fields[field_name] = []
            fields[field_name].append(row["new_name"])
    for k, v in fields.items():
        fields[k] = list(set(v))
    return fields


def print_field_summary(fields):
    sorted_fields = {}
    keys = sorted(deepcopy(fields), key=itemgetter(0))
    for k in keys:
        sorted_fields.update({k: fields[k]})
    print("")
    print(row_sep)
    print(f"| {'OLD NAME'.ljust(justify)} | {'NEW NAME'.ljust(justify)} |")
    print(row_sep)
    for k, v in sorted_fields.items():
        print(f"| {k.ljust(justify)} | {v[0].ljust(justify)} |")
        print(row_sep)


meta_screening_data = [
    dict(
        model_name="historicalicpreferral",
        old_name="hba1c",
        new_name="hba1c_value",
    ),
    dict(
        model_name="historicalicpreferral",
        old_name="fasting_glucose",
        new_name="ifg_value",
    ),
    dict(
        model_name="historicalicpreferral",
        old_name="ogtt_two_hr",
        new_name="ogtt_value",
    ),
    dict(
        model_name="historicalscreeningpartone",
        old_name="calculated_bmi",
        new_name="calculated_bmi_value",
    ),
    dict(
        model_name="historicalscreeningpartone",
        old_name="calculated_egfr",
        new_name="calculated_egfr_value",
    ),
    dict(
        model_name="historicalscreeningpartone",
        old_name="converted_creatinine",
        new_name="converted_creatinine_value",
    ),
    dict(
        model_name="historicalscreeningpartone",
        old_name="converted_fasting_glucose",
        new_name="converted_ifg_value",
    ),
    dict(
        model_name="historicalscreeningpartone",
        old_name="converted_ogtt_two_hr",
        new_name="converted_ogtt_value",
    ),
    dict(
        model_name="historicalscreeningpartone",
        old_name="creatinine",
        new_name="creatinine_value",
    ),
    dict(
        model_name="historicalscreeningpartone",
        old_name="hba1c",
        new_name="hba1c_value",
    ),
    dict(
        model_name="historicalscreeningpartone",
        old_name="ogtt_two_hr_datetime",
        new_name="ogtt_datetime",
    ),
    dict(
        model_name="historicalscreeningpartone",
        old_name="ogtt_two_hr_quantifier",
        new_name="ogtt_quantifier",
    ),
    dict(
        model_name="historicalscreeningpartone",
        old_name="urine_bhcg",
        new_name="urine_bhcg_value",
    ),
    dict(
        model_name="historicalscreeningpartthree",
        old_name="calculated_bmi",
        new_name="calculated_bmi_value",
    ),
    dict(
        model_name="historicalscreeningpartthree",
        old_name="calculated_egfr",
        new_name="calculated_egfr_value",
    ),
    dict(
        model_name="historicalscreeningpartthree",
        old_name="converted_creatinine",
        new_name="converted_creatinine_value",
    ),
    dict(
        model_name="historicalscreeningpartthree",
        old_name="converted_fasting_glucose",
        new_name="converted_ifg_value",
    ),
    dict(
        model_name="historicalscreeningpartthree",
        old_name="converted_ogtt_two_hr",
        new_name="converted_ogtt_value",
    ),
    dict(
        model_name="historicalscreeningpartthree",
        old_name="creatinine",
        new_name="creatinine_value",
    ),
    dict(
        model_name="historicalscreeningpartthree",
        old_name="hba1c",
        new_name="hba1c_value",
    ),
    dict(
        model_name="historicalscreeningpartthree",
        old_name="ogtt_two_hr_datetime",
        new_name="ogtt_datetime",
    ),
    dict(
        model_name="historicalscreeningpartthree",
        old_name="ogtt_two_hr_quantifier",
        new_name="ogtt_quantifier",
    ),
    dict(
        model_name="historicalscreeningpartthree",
        old_name="ogtt_two_hr_units",
        new_name="ogtt_units",
    ),
    dict(
        model_name="historicalscreeningpartthree",
        old_name="urine_bhcg",
        new_name="urine_bhcg_value",
    ),
    dict(
        model_name="historicalscreeningparttwo",
        old_name="calculated_bmi",
        new_name="calculated_bmi_value",
    ),
    dict(
        model_name="historicalscreeningparttwo",
        old_name="calculated_egfr",
        new_name="calculated_egfr_value",
    ),
    dict(
        model_name="historicalscreeningparttwo",
        old_name="converted_creatinine",
        new_name="converted_creatinine_value",
    ),
    dict(
        model_name="historicalscreeningparttwo",
        old_name="converted_fasting_glucose",
        new_name="converted_ifg_value",
    ),
    dict(
        model_name="historicalscreeningparttwo",
        old_name="converted_ogtt_two_hr",
        new_name="converted_ogtt_value",
    ),
    dict(
        model_name="historicalscreeningparttwo",
        old_name="creatinine",
        new_name="creatinine_value",
    ),
    dict(
        model_name="historicalscreeningparttwo",
        old_name="hba1c",
        new_name="hba1c_value",
    ),
    dict(
        model_name="historicalscreeningparttwo",
        old_name="ogtt_two_hr_datetime",
        new_name="ogtt_datetime",
    ),
    dict(
        model_name="historicalscreeningparttwo",
        old_name="ogtt_two_hr_quantifier",
        new_name="ogtt_quantifier",
    ),
    dict(
        model_name="historicalscreeningparttwo",
        old_name="ogtt_two_hr_units",
        new_name="ogtt_units",
    ),
    dict(
        model_name="historicalscreeningparttwo",
        old_name="urine_bhcg",
        new_name="urine_bhcg_value",
    ),
    dict(
        model_name="historicalsubjectscreening",
        old_name="calculated_bmi",
        new_name="calculated_bmi_value",
    ),
    dict(
        model_name="historicalsubjectscreening",
        old_name="calculated_egfr",
        new_name="calculated_egfr_value",
    ),
    dict(
        model_name="historicalsubjectscreening",
        old_name="converted_creatinine",
        new_name="converted_creatinine_value",
    ),
    dict(
        model_name="historicalsubjectscreening",
        old_name="converted_fasting_glucose",
        new_name="converted_ifg_value",
    ),
    dict(
        model_name="historicalsubjectscreening",
        old_name="converted_ogtt_two_hr",
        new_name="converted_ogtt_value",
    ),
    dict(
        model_name="historicalsubjectscreening",
        old_name="creatinine",
        new_name="creatinine_value",
    ),
    dict(
        model_name="historicalsubjectscreening",
        old_name="hba1c",
        new_name="hba1c_value",
    ),
    dict(
        model_name="historicalsubjectscreening",
        old_name="ogtt_two_hr_datetime",
        new_name="ogtt_datetime",
    ),
    dict(
        model_name="historicalsubjectscreening",
        old_name="ogtt_two_hr_quantifier",
        new_name="ogtt_quantifier",
    ),
    dict(
        model_name="historicalsubjectscreening",
        old_name="ogtt_two_hr_units",
        new_name="ogtt_units",
    ),
    dict(
        model_name="historicalsubjectscreening",
        old_name="urine_bhcg",
        new_name="urine_bhcg_value",
    ),
    dict(
        model_name="icpreferral",
        old_name="hba1c",
        new_name="hba1c_value",
    ),
    dict(
        model_name="icpreferral",
        old_name="fasting_glucose",
        new_name="ifg_value",
    ),
    dict(
        model_name="icpreferral",
        old_name="ogtt_two_hr",
        new_name="ogtt_value",
    ),
    dict(
        model_name="subjectscreening",
        old_name="calculated_bmi",
        new_name="calculated_bmi_value",
    ),
    dict(
        model_name="subjectscreening",
        old_name="calculated_egfr",
        new_name="calculated_egfr_value",
    ),
    dict(
        model_name="subjectscreening",
        old_name="converted_creatinine",
        new_name="converted_creatinine_value",
    ),
    dict(
        model_name="subjectscreening",
        old_name="converted_fasting_glucose",
        new_name="converted_ifg_value",
    ),
    dict(
        model_name="subjectscreening",
        old_name="converted_ogtt_two_hr",
        new_name="converted_ogtt_value",
    ),
    dict(
        model_name="subjectscreening",
        old_name="creatinine",
        new_name="creatinine_value",
    ),
    dict(
        model_name="subjectscreening",
        old_name="hba1c",
        new_name="hba1c_value",
    ),
    dict(
        model_name="subjectscreening",
        old_name="ogtt_two_hr_datetime",
        new_name="ogtt_datetime",
    ),
    dict(
        model_name="subjectscreening",
        old_name="ogtt_two_hr_quantifier",
        new_name="ogtt_quantifier",
    ),
    dict(
        model_name="subjectscreening",
        old_name="ogtt_two_hr_units",
        new_name="ogtt_units",
    ),
    dict(
        model_name="subjectscreening",
        old_name="urine_bhcg",
        new_name="urine_bhcg_value",
    ),
    dict(
        model_name="historicalscreeningpartone",
        old_name="fasting_glucose",
        new_name="ifg_value",
    ),
    dict(
        model_name="historicalscreeningpartone",
        old_name="fasting_glucose_datetime",
        new_name="ifg_datetime",
    ),
    dict(
        model_name="historicalscreeningpartone",
        old_name="fasting_glucose_quantifier",
        new_name="ifg_quantifier",
    ),
    dict(
        model_name="historicalscreeningpartone",
        old_name="fasting_glucose_units",
        new_name="ifg_units",
    ),
    dict(
        model_name="historicalscreeningpartone",
        old_name="ogtt_two_hr",
        new_name="ogtt_value",
    ),
    dict(
        model_name="historicalscreeningpartone",
        old_name="ogtt_two_hr_units",
        new_name="ogtt_units",
    ),
    dict(
        model_name="historicalscreeningpartthree",
        old_name="fasting_glucose",
        new_name="ifg_value",
    ),
    dict(
        model_name="historicalscreeningpartthree",
        old_name="fasting_glucose_datetime",
        new_name="ifg_datetime",
    ),
    dict(
        model_name="historicalscreeningpartthree",
        old_name="fasting_glucose_quantifier",
        new_name="ifg_quantifier",
    ),
    dict(
        model_name="historicalscreeningpartthree",
        old_name="fasting_glucose_units",
        new_name="ifg_units",
    ),
    dict(
        model_name="historicalscreeningpartthree",
        old_name="ogtt_two_hr",
        new_name="ogtt_value",
    ),
    dict(
        model_name="historicalscreeningparttwo",
        old_name="fasting_glucose",
        new_name="ifg_value",
    ),
    dict(
        model_name="historicalscreeningparttwo",
        old_name="fasting_glucose_datetime",
        new_name="ifg_datetime",
    ),
    dict(
        model_name="historicalscreeningparttwo",
        old_name="fasting_glucose_quantifier",
        new_name="ifg_quantifier",
    ),
    dict(
        model_name="historicalscreeningparttwo",
        old_name="fasting_glucose_units",
        new_name="ifg_units",
    ),
    dict(
        model_name="historicalscreeningparttwo",
        old_name="ogtt_two_hr",
        new_name="ogtt_value",
    ),
    dict(
        model_name="historicalsubjectscreening",
        old_name="fasting_glucose",
        new_name="ifg_value",
    ),
    dict(
        model_name="historicalsubjectscreening",
        old_name="fasting_glucose_datetime",
        new_name="ifg_datetime",
    ),
    dict(
        model_name="historicalsubjectscreening",
        old_name="fasting_glucose_quantifier",
        new_name="ifg_quantifier",
    ),
    dict(
        model_name="historicalsubjectscreening",
        old_name="fasting_glucose_units",
        new_name="ifg_units",
    ),
    dict(
        model_name="historicalsubjectscreening",
        old_name="ogtt_two_hr",
        new_name="ogtt_value",
    ),
    dict(
        model_name="subjectscreening",
        old_name="fasting_glucose",
        new_name="ifg_value",
    ),
    dict(
        model_name="subjectscreening",
        old_name="fasting_glucose_datetime",
        new_name="ifg_datetime",
    ),
    dict(
        model_name="subjectscreening",
        old_name="fasting_glucose_quantifier",
        new_name="ifg_quantifier",
    ),
    dict(
        model_name="subjectscreening",
        old_name="fasting_glucose_units",
        new_name="ifg_units",
    ),
    dict(
        model_name="subjectscreening",
        old_name="ogtt_two_hr",
        new_name="ogtt_value",
    ),
    dict(
        model_name="historicalscreeningpartone",
        old_name="fasted",
        new_name="fasting",
    ),
    dict(
        model_name="historicalscreeningpartone",
        old_name="fasted_duration_minutes",
        new_name="fasting_duration_minutes",
    ),
    dict(
        model_name="historicalscreeningpartone",
        old_name="fasted_duration_str",
        new_name="fasting_duration_str",
    ),
    dict(
        model_name="historicalscreeningpartthree",
        old_name="fasted",
        new_name="fasting",
    ),
    dict(
        model_name="historicalscreeningpartthree",
        old_name="fasted_duration_minutes",
        new_name="fasting_duration_minutes",
    ),
    dict(
        model_name="historicalscreeningpartthree",
        old_name="fasted_duration_str",
        new_name="fasting_duration_str",
    ),
    dict(
        model_name="historicalscreeningparttwo",
        old_name="fasted",
        new_name="fasting",
    ),
    dict(
        model_name="historicalscreeningparttwo",
        old_name="fasted_duration_minutes",
        new_name="fasting_duration_minutes",
    ),
    dict(
        model_name="historicalscreeningparttwo",
        old_name="fasted_duration_str",
        new_name="fasting_duration_str",
    ),
    dict(
        model_name="historicalsubjectscreening",
        old_name="fasted",
        new_name="fasting",
    ),
    dict(
        model_name="historicalsubjectscreening",
        old_name="fasted_duration_minutes",
        new_name="fasting_duration_minutes",
    ),
    dict(
        model_name="historicalsubjectscreening",
        old_name="fasted_duration_str",
        new_name="fasting_duration_str",
    ),
    dict(
        model_name="subjectscreening",
        old_name="fasted",
        new_name="fasting",
    ),
    dict(
        model_name="subjectscreening",
        old_name="fasted_duration_minutes",
        new_name="fasting_duration_minutes",
    ),
    dict(
        model_name="subjectscreening",
        old_name="fasted_duration_str",
        new_name="fasting_duration_str",
    ),
]

meta_subject_data = [
    dict(
        model_name="historicalpatienthistory",
        old_name="hypertension_diagnosis",
        new_name="htn_diagnosis",
    ),
    dict(
        model_name="patienthistory",
        old_name="hypertension_diagnosis",
        new_name="htn_diagnosis",
    ),
    dict(
        model_name="bloodresultsfbc",
        old_name="fbc_assay_datetime",
        new_name="assay_datetime",
    ),
    dict(
        model_name="bloodresultsfbc",
        old_name="haemoglobin",
        new_name="haemoglobin_value",
    ),
    dict(
        model_name="bloodresultsfbc",
        old_name="hct",
        new_name="hct_value",
    ),
    dict(
        model_name="bloodresultsfbc",
        old_name="platelets",
        new_name="platelets_value",
    ),
    dict(
        model_name="bloodresultsfbc",
        old_name="rbc",
        new_name="rbc_value",
    ),
    dict(
        model_name="bloodresultsfbc",
        old_name="wbc",
        new_name="wbc_value",
    ),
    dict(
        model_name="bloodresultsglu",
        old_name="glucose_assay_datetime",
        new_name="assay_datetime",
    ),
    dict(
        model_name="bloodresultsglu",
        old_name="glucose_abnormal",
        new_name="gluc_abnormal",
    ),
    dict(
        model_name="bloodresultsglu",
        old_name="glucose_quantifier",
        new_name="gluc_quantifier",
    ),
    dict(
        model_name="bloodresultsglu",
        old_name="glucose_reportable",
        new_name="gluc_reportable",
    ),
    dict(
        model_name="bloodresultsglu",
        old_name="glucose_units",
        new_name="gluc_units",
    ),
    dict(
        model_name="bloodresultsglu",
        old_name="glucose",
        new_name="gluc_value",
    ),
    dict(
        model_name="bloodresultshba1c",
        old_name="hba1c_assay_datetime",
        new_name="assay_datetime",
    ),
    dict(
        model_name="bloodresultslft",
        old_name="albumin",
        new_name="albumin_value",
    ),
    dict(
        model_name="bloodresultslft",
        old_name="alp",
        new_name="alp_value",
    ),
    dict(
        model_name="bloodresultslft",
        old_name="alt",
        new_name="alt_value",
    ),
    dict(
        model_name="bloodresultslft",
        old_name="lft_assay_datetime",
        new_name="assay_datetime",
    ),
    dict(
        model_name="bloodresultslft",
        old_name="ast",
        new_name="ast_value",
    ),
    dict(
        model_name="bloodresultslft",
        old_name="ggt",
        new_name="ggt_value",
    ),
    dict(
        model_name="bloodresultslipid",
        old_name="lipid_assay_datetime",
        new_name="assay_datetime",
    ),
    dict(
        model_name="bloodresultsrft",
        old_name="rft_assay_datetime",
        new_name="assay_datetime",
    ),
    dict(
        model_name="bloodresultsrft",
        old_name="egfr",
        new_name="egfr_value",
    ),
    dict(
        model_name="bloodresultsrft",
        old_name="urea",
        new_name="urea_value",
    ),
    dict(
        model_name="bloodresultsrft",
        old_name="uric_acid",
        new_name="uric_acid_value",
    ),
    dict(
        model_name="glucose",
        old_name="ogtt_two_hr_datetime",
        new_name="ogtt_datetime",
    ),
    dict(
        model_name="glucose",
        old_name="ogtt_two_hr_quantifier",
        new_name="ogtt_quantifier",
    ),
    dict(
        model_name="glucose",
        old_name="ogtt_two_hr_units",
        new_name="ogtt_units",
    ),
    dict(
        model_name="historicalbloodresultsfbc",
        old_name="fbc_assay_datetime",
        new_name="assay_datetime",
    ),
    dict(
        model_name="historicalbloodresultsfbc",
        old_name="haemoglobin",
        new_name="haemoglobin_value",
    ),
    dict(
        model_name="historicalbloodresultsfbc",
        old_name="hct",
        new_name="hct_value",
    ),
    dict(
        model_name="historicalbloodresultsfbc",
        old_name="platelets",
        new_name="platelets_value",
    ),
    dict(
        model_name="historicalbloodresultsfbc",
        old_name="rbc",
        new_name="rbc_value",
    ),
    dict(
        model_name="historicalbloodresultsfbc",
        old_name="fbc_requisition",
        new_name="requisition",
    ),
    dict(
        model_name="historicalbloodresultsfbc",
        old_name="wbc",
        new_name="wbc_value",
    ),
    dict(
        model_name="historicalbloodresultsglu",
        old_name="glucose_assay_datetime",
        new_name="assay_datetime",
    ),
    dict(
        model_name="historicalbloodresultsglu",
        old_name="glucose_abnormal",
        new_name="gluc_abnormal",
    ),
    dict(
        model_name="historicalbloodresultsglu",
        old_name="glucose_quantifier",
        new_name="gluc_quantifier",
    ),
    dict(
        model_name="historicalbloodresultsglu",
        old_name="glucose_reportable",
        new_name="gluc_reportable",
    ),
    dict(
        model_name="historicalbloodresultsglu",
        old_name="glucose_units",
        new_name="gluc_units",
    ),
    dict(
        model_name="historicalbloodresultsglu",
        old_name="glucose",
        new_name="gluc_value",
    ),
    dict(
        model_name="historicalbloodresultsglu",
        old_name="glucose_requisition",
        new_name="requisition",
    ),
    dict(
        model_name="historicalbloodresultshba1c",
        old_name="hba1c_assay_datetime",
        new_name="assay_datetime",
    ),
    dict(
        model_name="historicalbloodresultshba1c",
        old_name="hba1c_requisition",
        new_name="requisition",
    ),
    dict(
        model_name="historicalbloodresultslft",
        old_name="albumin",
        new_name="albumin_value",
    ),
    dict(
        model_name="historicalbloodresultslft",
        old_name="alp",
        new_name="alp_value",
    ),
    dict(
        model_name="historicalbloodresultslft",
        old_name="alt",
        new_name="alt_value",
    ),
    dict(
        model_name="historicalbloodresultslft",
        old_name="lft_assay_datetime",
        new_name="assay_datetime",
    ),
    dict(
        model_name="historicalbloodresultslft",
        old_name="ast",
        new_name="ast_value",
    ),
    dict(
        model_name="historicalbloodresultslft",
        old_name="ggt",
        new_name="ggt_value",
    ),
    dict(
        model_name="historicalbloodresultslft",
        old_name="lft_requisition",
        new_name="requisition",
    ),
    dict(
        model_name="historicalbloodresultslipid",
        old_name="lipid_assay_datetime",
        new_name="assay_datetime",
    ),
    dict(
        model_name="historicalbloodresultslipid",
        old_name="lipid_requisition",
        new_name="requisition",
    ),
    dict(
        model_name="historicalbloodresultsrft",
        old_name="rft_assay_datetime",
        new_name="assay_datetime",
    ),
    dict(
        model_name="historicalbloodresultsrft",
        old_name="egfr",
        new_name="egfr_value",
    ),
    dict(
        model_name="historicalbloodresultsrft",
        old_name="rft_requisition",
        new_name="requisition",
    ),
    dict(
        model_name="historicalbloodresultsrft",
        old_name="urea",
        new_name="urea_value",
    ),
    dict(
        model_name="historicalbloodresultsrft",
        old_name="uric_acid",
        new_name="uric_acid_value",
    ),
    dict(
        model_name="historicalglucose",
        old_name="ogtt_two_hr_datetime",
        new_name="ogtt_datetime",
    ),
    dict(
        model_name="historicalglucose",
        old_name="ogtt_two_hr_quantifier",
        new_name="ogtt_quantifier",
    ),
    dict(
        model_name="historicalglucose",
        old_name="ogtt_two_hr_units",
        new_name="ogtt_units",
    ),
    #
    #
    #
    dict(
        model_name="bloodresultsfbc",
        old_name="fbc_requisition",
        new_name="requisition",
    ),
    dict(
        model_name="bloodresultsglu",
        old_name="glucose_requisition",
        new_name="requisition",
    ),
    dict(
        model_name="bloodresultshba1c",
        old_name="hba1c",
        new_name="hba1c_value",
    ),
    dict(
        model_name="bloodresultshba1c",
        old_name="hba1c_requisition",
        new_name="requisition",
    ),
    dict(
        model_name="bloodresultslft",
        old_name="amylase",
        new_name="amylase_value",
    ),
    dict(
        model_name="bloodresultslft",
        old_name="lft_requisition",
        new_name="requisition",
    ),
    dict(
        model_name="bloodresultslipid",
        old_name="lipid_requisition",
        new_name="requisition",
    ),
    dict(
        model_name="bloodresultsrft",
        old_name="creatinine",
        new_name="creatinine_value",
    ),
    dict(
        model_name="bloodresultsrft",
        old_name="rft_requisition",
        new_name="requisition",
    ),
    dict(
        model_name="glucose",
        old_name="fasting_glucose",
        new_name="ifg_value",
    ),
    dict(
        model_name="glucose",
        old_name="fasting_glucose_datetime",
        new_name="ifg_datetime",
    ),
    dict(
        model_name="glucose",
        old_name="fasting_glucose_quantifier",
        new_name="ifg_quantifier",
    ),
    dict(
        model_name="glucose",
        old_name="fasting_glucose_units",
        new_name="ifg_units",
    ),
    dict(
        model_name="glucose",
        old_name="ogtt_two_hr",
        new_name="ogtt_value",
    ),
    dict(
        model_name="historicalbloodresultshba1c",
        old_name="hba1c",
        new_name="hba1c_value",
    ),
    dict(
        model_name="historicalbloodresultslft",
        old_name="amylase",
        new_name="amylase_value",
    ),
    dict(
        model_name="historicalbloodresultsrft",
        old_name="creatinine",
        new_name="creatinine_value",
    ),
    dict(
        model_name="historicalglucose",
        old_name="fasting_glucose",
        new_name="ifg_value",
    ),
    dict(
        model_name="historicalglucose",
        old_name="fasting_glucose_datetime",
        new_name="ifg_datetime",
    ),
    dict(
        model_name="historicalglucose",
        old_name="fasting_glucose_quantifier",
        new_name="ifg_quantifier",
    ),
    dict(
        model_name="historicalglucose",
        old_name="fasting_glucose_units",
        new_name="ifg_units",
    ),
    dict(
        model_name="historicalglucose",
        old_name="ogtt_two_hr",
        new_name="ogtt_value",
    ),
    dict(
        model_name="bloodresultslipid",
        old_name="hdl",
        new_name="hdl_value",
    ),
    dict(
        model_name="bloodresultslipid",
        old_name="ldl",
        new_name="ldl_value",
    ),
    dict(
        model_name="bloodresultslipid",
        old_name="trig",
        new_name="trig_value",
    ),
    dict(
        model_name="historicalbloodresultslipid",
        old_name="hdl",
        new_name="hdl_value",
    ),
    dict(
        model_name="historicalbloodresultslipid",
        old_name="ldl",
        new_name="ldl_value",
    ),
    dict(
        model_name="historicalbloodresultslipid",
        old_name="trig",
        new_name="trig_value",
    ),
    dict(
        model_name="bloodresultsglu",
        old_name="gluc_abnormal",
        new_name="glucose_abnormal",
    ),
    dict(
        model_name="bloodresultsglu",
        old_name="gluc_quantifier",
        new_name="glucose_quantifier",
    ),
    dict(
        model_name="bloodresultsglu",
        old_name="gluc_reportable",
        new_name="glucose_reportable",
    ),
    dict(
        model_name="bloodresultsglu",
        old_name="gluc_units",
        new_name="glucose_units",
    ),
    dict(
        model_name="historicalbloodresultsglu",
        old_name="gluc_abnormal",
        new_name="glucose_abnormal",
    ),
    dict(
        model_name="historicalbloodresultsglu",
        old_name="gluc_quantifier",
        new_name="glucose_quantifier",
    ),
    dict(
        model_name="historicalbloodresultsglu",
        old_name="gluc_reportable",
        new_name="glucose_reportable",
    ),
    dict(
        model_name="historicalbloodresultsglu",
        old_name="gluc_units",
        new_name="glucose_units",
    ),
    dict(
        model_name="bloodresultsglu",
        old_name="gluc_value",
        new_name="glucose_value",
    ),
    dict(
        model_name="historicalbloodresultsglu",
        old_name="gluc_value",
        new_name="glucose_value",
    ),
    dict(
        model_name="glucose",
        old_name="fasted",
        new_name="fasting",
    ),
    dict(
        model_name="glucose",
        old_name="fasted_duration_minutes",
        new_name="fasting_duration_minutes",
    ),
    dict(
        model_name="glucose",
        old_name="fasted_duration_str",
        new_name="fasting_duration_str",
    ),
    dict(
        model_name="historicalglucose",
        old_name="fasted",
        new_name="fasting",
    ),
    dict(
        model_name="historicalglucose",
        old_name="fasted_duration_minutes",
        new_name="fasting_duration_minutes",
    ),
    dict(
        model_name="historicalglucose",
        old_name="fasted_duration_str",
        new_name="fasting_duration_str",
    ),
]

# print_table(meta_screening_data, "meta_screening")
# print_table(meta_subject_data, "meta_subject")
# meta_fields = fields_summary(meta_screening_data)
# meta_fields = fields_summary(meta_screening_data, fields=meta_fields)
# print_field_summary(meta_fields)

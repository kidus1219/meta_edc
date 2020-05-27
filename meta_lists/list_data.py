from edc_constants.constants import LOST_TO_FOLLOWUP, OTHER, UNKNOWN, DEAD, NONE
from edc_list_data import PreloadData
from meta_prn.constants import (
    WITHDRAWAL,
    TRANSFERRED,
    LATE_EXCLUSION,
    OTHER_RX_DISCONTINUATION,
)


list_data = {
    "meta_lists.nonadherencereasons": [
        ("forget_to_take", "I sometimes forget to take my pills"),
        ("dont_like_taking", "I don't like taking my pills"),
        ("make_me_ill", "My pills sometimes make me feel sick"),
        ("misplaced_pills", "I sometimes misplace my pills"),
        ("dont_believe_pills_help", "I don't believe my pills are helping me"),
        ("dont_believe_pills_needed", "I don't believe I need to take my pills"),
        ("not_feeling_well", "I have not been feeling well"),
        (OTHER, "Other, please specify ..."),
    ],
    "meta_lists.hypertensionmedications": [
        ("amlodipine", "Amlodipine"),
        ("atenolol", "Atenolol"),
        ("bendroflumethiazide", "Bendroflumethiazide"),
        ("bisoprolol", "Bisoprolol"),
        ("captopril", "Captopril"),
        ("diltiazem", "Diltiazem"),
        ("enalapril", "Enalapril"),
        ("eplerenone", "Eplerenone"),
        ("furosemide", "Furosemide"),
        ("hydralazine", "Hydralazine"),
        ("hydrochlothiazide", "Hydrochlothiazide"),
        ("indapamide", "Indapamide"),
        ("losartan", "Losartan"),
        ("metoprolol", "Metoprolol"),
        ("nifedipine", "Nifedipine"),
        ("perindopril", "Perindopril"),
        ("propanolol", "Propanolol"),
        ("spironolactone", "Spironolactone"),
        ("telmisartan", "Telmisartan"),
        ("torsemide", "Torsemide"),
        ("verapamil", "Verapamil"),
        (OTHER, "Other, specify"),
    ],
    "meta_lists.diabetessymptoms": [
        ("frequent_urination", "Wanting to urinate more often than usual"),
        ("excessive_thirst", "Wanting to drink water more than usual"),
        ("excessive_eating", "Wanting to eat food more than usual"),
        (OTHER, "Other, specify"),
        (NONE, "No symptoms to report"),
    ],
    "meta_lists.oiprophylaxis": [
        ("tmp_smx", "TMP/SMX"),
        ("fluconazole", "Fluconazole"),
        ("isoniazid", "Isoniazid"),
        (OTHER, "Other, specify"),
    ],
    "meta_lists.symptoms": [
        ("nausea", "Nausea"),
        ("vomiting", "Vomiting"),
        ("abdominal_pain_general", "Abdominal pain (General)"),
        ("abdominal_pain_right_upper_quad", "Abdominal pain (Right upper quadrant)"),
        ("loss_of_appetite", "Loss of appetite"),
        ("flatulence", "Flatulence (gas)"),
        ("dizziness", "Dizziness"),
        ("shakiness", "Shakiness"),
        ("headaches", "Headaches"),
        ("sweating", "Sweating"),
        ("fatigue", "Fatigue"),
        ("weakness", "Weakness"),
        ("muscle_pain", "Muscle pain"),
        ("muscle_cramping", "Muscle cramping"),
        ("pounding_heartbeat", "Fast or pounding heartbeat"),
        ("shallow_breathing", "Fast or shallow breathing"),
        ("unusual_sleepiness", "Unusual sleepiness"),
        (NONE, "No symptoms to report"),
        (OTHER, "Other, specify"),
    ],
    "meta_lists.baselinesymptoms": [
        ("loss_of_weight", "Loss of weight"),
        ("skin_infection", "Skin infection"),
        ("sweating", "Sweating"),
        ("vomiting", "Vomiting"),
        ("headaches", "Headaches"),
        ("shakiness", "Shakiness"),
        ("dizziness", "Dizziness"),
        ("unusual_sleepiness", "Unusual sleepiness"),
        ("shallow_breathing", "Fast or shallow breathing"),
        ("muscle_cramping", "Muscle cramping"),
        ("weakness", "Weakness"),
        ("fatigue", "Fatigue"),
        ("cough", "Cough"),
        ("loss_of_appetite", "Loss of appetite"),
        ("diarrhoea", "Diarrhoea"),
        ("abdominal_pain_general", "Abdominal pain (General)"),
        (NONE, "No symptoms to report"),
        (OTHER, "Other, specify"),
    ],
    "meta_lists.arvregimens": [
        ("TDF_3TC_ATV_r", "TDF + 3TC + ATV/r"),
        ("TDF_FTC_ATV_r", "TDF + FTC + ATV/r"),
        ("TDF_3TC_LPV_r", "TDF + 3TC + LPV/r"),
        ("AZT_3TC_ATV_r", "AZT + 3TC + ATV/r"),
        ("AZT_3TC_LPV_r", "AZT + 3TC + LPV/r"),
        ("ABC_3TC_ATV_r", "ABC + 3TC + ATV/r"),
        ("ABC_3TC_LPV_r", "ABC + 3TC + LPV/r"),
        ("TDF_FTC_LPV_r", "TDF + FTC + LPV/r"),
        ("DTG_ABC/3TC_ATV_r", "DTG + (ABC/3TC) + ATV/r"),
        (UNKNOWN, "Unknown"),
        (OTHER, "Other, specify"),
    ],
    "meta_lists.offstudyreasons": [
        ("completed_followup", "Patient completed 12 months of follow-up"),
        ("clinical_endpoint", "Patient reached a clinical endpoint"),
        ("toxicity", "Patient experienced an unacceptable toxicity"),
        (
            "intercurrent_illness",
            "Intercurrent illness which prevents further treatment",
        ),
        (LOST_TO_FOLLOWUP, "Patient lost to follow-up"),
        (DEAD, "Patient reported/known to have died"),
        (WITHDRAWAL, "Patient withdrew consent to participate further"),
        (LATE_EXCLUSION, "Patient fulfilled late exclusion criteria*"),
        (TRANSFERRED, "Patient has been transferred to another health centre"),
        (
            OTHER_RX_DISCONTINUATION,
            "Other condition that justifies the discontinuation of "
            "treatment in the clinician’s opinion (specify below)",
        ),
        (OTHER, "Other reason (specify below)",),
    ],
    "meta_lists.missedvisitreasons": [
        ("forgot", "Forgot / Can’t remember being told about appointment"),
        ("familt_emergency", "Family emergency (e.g. funeral) and was away"),
        ("travelling", "Away travelling/visiting"),
        ("working_schooling", "Away working/schooling"),
        ("too_sick", "Too sick or weak to come to the centre"),
        ("lack_of_transport", "Transportation difficulty"),
        (OTHER, "Other reason (specify below)",),
    ],
}

preload_data = PreloadData(list_data=list_data)

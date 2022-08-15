# Generated by Django 3.2.11 on 2022-07-22 18:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("meta_subject", "0132_auto_20220722_1825"),
    ]

    operations = [
        migrations.AddField(
            model_name="bloodresultsfbc",
            name="haemoglobin_quantifier",
            field=models.CharField(
                blank=True,
                choices=[("=", "="), (">", ">"), (">=", ">="), ("<", "<"), ("<=", "<=")],
                default="=",
                max_length=10,
                null=True,
                verbose_name="Quantifier",
            ),
        ),
        migrations.AddField(
            model_name="bloodresultsfbc",
            name="hct_quantifier",
            field=models.CharField(
                blank=True,
                choices=[("=", "="), (">", ">"), (">=", ">="), ("<", "<"), ("<=", "<=")],
                default="=",
                max_length=10,
                null=True,
                verbose_name="Quantifier",
            ),
        ),
        migrations.AddField(
            model_name="bloodresultsfbc",
            name="mch_quantifier",
            field=models.CharField(
                blank=True,
                choices=[("=", "="), (">", ">"), (">=", ">="), ("<", "<"), ("<=", "<=")],
                default="=",
                max_length=10,
                null=True,
                verbose_name="Quantifier",
            ),
        ),
        migrations.AddField(
            model_name="bloodresultsfbc",
            name="mchc_quantifier",
            field=models.CharField(
                blank=True,
                choices=[("=", "="), (">", ">"), (">=", ">="), ("<", "<"), ("<=", "<=")],
                default="=",
                max_length=10,
                null=True,
                verbose_name="Quantifier",
            ),
        ),
        migrations.AddField(
            model_name="bloodresultsfbc",
            name="mcv_quantifier",
            field=models.CharField(
                blank=True,
                choices=[("=", "="), (">", ">"), (">=", ">="), ("<", "<"), ("<=", "<=")],
                default="=",
                max_length=10,
                null=True,
                verbose_name="Quantifier",
            ),
        ),
        migrations.AddField(
            model_name="bloodresultsfbc",
            name="platelets_quantifier",
            field=models.CharField(
                blank=True,
                choices=[("=", "="), (">", ">"), (">=", ">="), ("<", "<"), ("<=", "<=")],
                default="=",
                max_length=10,
                null=True,
                verbose_name="Quantifier",
            ),
        ),
        migrations.AddField(
            model_name="bloodresultsfbc",
            name="rbc_quantifier",
            field=models.CharField(
                blank=True,
                choices=[("=", "="), (">", ">"), (">=", ">="), ("<", "<"), ("<=", "<=")],
                default="=",
                max_length=10,
                null=True,
                verbose_name="Quantifier",
            ),
        ),
        migrations.AddField(
            model_name="bloodresultsfbc",
            name="wbc_quantifier",
            field=models.CharField(
                blank=True,
                choices=[("=", "="), (">", ">"), (">=", ">="), ("<", "<"), ("<=", "<=")],
                default="=",
                max_length=10,
                null=True,
                verbose_name="Quantifier",
            ),
        ),
        migrations.AddField(
            model_name="bloodresultsins",
            name="ins_grade",
            field=models.IntegerField(
                blank=True,
                choices=[
                    (0, "Not graded"),
                    (1, "Grade 1"),
                    (2, "Grade 2"),
                    (3, "Grade 3"),
                    (4, "Grade 4"),
                    (5, "Grade 5"),
                ],
                null=True,
                verbose_name="Grade",
            ),
        ),
        migrations.AddField(
            model_name="bloodresultsins",
            name="ins_grade_description",
            field=models.CharField(
                blank=True, max_length=250, null=True, verbose_name="Grade description"
            ),
        ),
        migrations.AddField(
            model_name="bloodresultslft",
            name="albumin_quantifier",
            field=models.CharField(
                blank=True,
                choices=[("=", "="), (">", ">"), (">=", ">="), ("<", "<"), ("<=", "<=")],
                default="=",
                max_length=10,
                null=True,
                verbose_name="Quantifier",
            ),
        ),
        migrations.AddField(
            model_name="bloodresultslft",
            name="alp_quantifier",
            field=models.CharField(
                blank=True,
                choices=[("=", "="), (">", ">"), (">=", ">="), ("<", "<"), ("<=", "<=")],
                default="=",
                max_length=10,
                null=True,
                verbose_name="Quantifier",
            ),
        ),
        migrations.AddField(
            model_name="bloodresultslft",
            name="alt_quantifier",
            field=models.CharField(
                blank=True,
                choices=[("=", "="), (">", ">"), (">=", ">="), ("<", "<"), ("<=", "<=")],
                default="=",
                max_length=10,
                null=True,
                verbose_name="Quantifier",
            ),
        ),
        migrations.AddField(
            model_name="bloodresultslft",
            name="amylase_quantifier",
            field=models.CharField(
                blank=True,
                choices=[("=", "="), (">", ">"), (">=", ">="), ("<", "<"), ("<=", "<=")],
                default="=",
                max_length=10,
                null=True,
                verbose_name="Quantifier",
            ),
        ),
        migrations.AddField(
            model_name="bloodresultslft",
            name="ast_quantifier",
            field=models.CharField(
                blank=True,
                choices=[("=", "="), (">", ">"), (">=", ">="), ("<", "<"), ("<=", "<=")],
                default="=",
                max_length=10,
                null=True,
                verbose_name="Quantifier",
            ),
        ),
        migrations.AddField(
            model_name="bloodresultslft",
            name="ggt_quantifier",
            field=models.CharField(
                blank=True,
                choices=[("=", "="), (">", ">"), (">=", ">="), ("<", "<"), ("<=", "<=")],
                default="=",
                max_length=10,
                null=True,
                verbose_name="Quantifier",
            ),
        ),
        migrations.AddField(
            model_name="bloodresultslipid",
            name="chol_quantifier",
            field=models.CharField(
                blank=True,
                choices=[("=", "="), (">", ">"), (">=", ">="), ("<", "<"), ("<=", "<=")],
                default="=",
                max_length=10,
                null=True,
                verbose_name="Quantifier",
            ),
        ),
        migrations.AddField(
            model_name="bloodresultslipid",
            name="hdl_quantifier",
            field=models.CharField(
                blank=True,
                choices=[("=", "="), (">", ">"), (">=", ">="), ("<", "<"), ("<=", "<=")],
                default="=",
                max_length=10,
                null=True,
                verbose_name="Quantifier",
            ),
        ),
        migrations.AddField(
            model_name="bloodresultslipid",
            name="ldl_quantifier",
            field=models.CharField(
                blank=True,
                choices=[("=", "="), (">", ">"), (">=", ">="), ("<", "<"), ("<=", "<=")],
                default="=",
                max_length=10,
                null=True,
                verbose_name="Quantifier",
            ),
        ),
        migrations.AddField(
            model_name="bloodresultslipid",
            name="trig_quantifier",
            field=models.CharField(
                blank=True,
                choices=[("=", "="), (">", ">"), (">=", ">="), ("<", "<"), ("<=", "<=")],
                default="=",
                max_length=10,
                null=True,
                verbose_name="Quantifier",
            ),
        ),
        migrations.AddField(
            model_name="bloodresultsrft",
            name="creatinine_quantifier",
            field=models.CharField(
                blank=True,
                choices=[("=", "="), (">", ">"), (">=", ">="), ("<", "<"), ("<=", "<=")],
                default="=",
                max_length=10,
                null=True,
                verbose_name="Quantifier",
            ),
        ),
        migrations.AddField(
            model_name="bloodresultsrft",
            name="egfr_drop_quantifier",
            field=models.CharField(
                blank=True,
                choices=[("=", "="), (">", ">"), (">=", ">="), ("<", "<"), ("<=", "<=")],
                default="=",
                max_length=10,
                null=True,
                verbose_name="Quantifier",
            ),
        ),
        migrations.AddField(
            model_name="bloodresultsrft",
            name="egfr_quantifier",
            field=models.CharField(
                blank=True,
                choices=[("=", "="), (">", ">"), (">=", ">="), ("<", "<"), ("<=", "<=")],
                default="=",
                max_length=10,
                null=True,
                verbose_name="Quantifier",
            ),
        ),
        migrations.AddField(
            model_name="bloodresultsrft",
            name="urea_quantifier",
            field=models.CharField(
                blank=True,
                choices=[("=", "="), (">", ">"), (">=", ">="), ("<", "<"), ("<=", "<=")],
                default="=",
                max_length=10,
                null=True,
                verbose_name="Quantifier",
            ),
        ),
        migrations.AddField(
            model_name="bloodresultsrft",
            name="uric_acid_quantifier",
            field=models.CharField(
                blank=True,
                choices=[("=", "="), (">", ">"), (">=", ">="), ("<", "<"), ("<=", "<=")],
                default="=",
                max_length=10,
                null=True,
                verbose_name="Quantifier",
            ),
        ),
        migrations.AddField(
            model_name="historicalbloodresultsfbc",
            name="haemoglobin_quantifier",
            field=models.CharField(
                blank=True,
                choices=[("=", "="), (">", ">"), (">=", ">="), ("<", "<"), ("<=", "<=")],
                default="=",
                max_length=10,
                null=True,
                verbose_name="Quantifier",
            ),
        ),
        migrations.AddField(
            model_name="historicalbloodresultsfbc",
            name="hct_quantifier",
            field=models.CharField(
                blank=True,
                choices=[("=", "="), (">", ">"), (">=", ">="), ("<", "<"), ("<=", "<=")],
                default="=",
                max_length=10,
                null=True,
                verbose_name="Quantifier",
            ),
        ),
        migrations.AddField(
            model_name="historicalbloodresultsfbc",
            name="mch_quantifier",
            field=models.CharField(
                blank=True,
                choices=[("=", "="), (">", ">"), (">=", ">="), ("<", "<"), ("<=", "<=")],
                default="=",
                max_length=10,
                null=True,
                verbose_name="Quantifier",
            ),
        ),
        migrations.AddField(
            model_name="historicalbloodresultsfbc",
            name="mchc_quantifier",
            field=models.CharField(
                blank=True,
                choices=[("=", "="), (">", ">"), (">=", ">="), ("<", "<"), ("<=", "<=")],
                default="=",
                max_length=10,
                null=True,
                verbose_name="Quantifier",
            ),
        ),
        migrations.AddField(
            model_name="historicalbloodresultsfbc",
            name="mcv_quantifier",
            field=models.CharField(
                blank=True,
                choices=[("=", "="), (">", ">"), (">=", ">="), ("<", "<"), ("<=", "<=")],
                default="=",
                max_length=10,
                null=True,
                verbose_name="Quantifier",
            ),
        ),
        migrations.AddField(
            model_name="historicalbloodresultsfbc",
            name="platelets_quantifier",
            field=models.CharField(
                blank=True,
                choices=[("=", "="), (">", ">"), (">=", ">="), ("<", "<"), ("<=", "<=")],
                default="=",
                max_length=10,
                null=True,
                verbose_name="Quantifier",
            ),
        ),
        migrations.AddField(
            model_name="historicalbloodresultsfbc",
            name="rbc_quantifier",
            field=models.CharField(
                blank=True,
                choices=[("=", "="), (">", ">"), (">=", ">="), ("<", "<"), ("<=", "<=")],
                default="=",
                max_length=10,
                null=True,
                verbose_name="Quantifier",
            ),
        ),
        migrations.AddField(
            model_name="historicalbloodresultsfbc",
            name="wbc_quantifier",
            field=models.CharField(
                blank=True,
                choices=[("=", "="), (">", ">"), (">=", ">="), ("<", "<"), ("<=", "<=")],
                default="=",
                max_length=10,
                null=True,
                verbose_name="Quantifier",
            ),
        ),
        migrations.AddField(
            model_name="historicalbloodresultsins",
            name="ins_grade",
            field=models.IntegerField(
                blank=True,
                choices=[
                    (0, "Not graded"),
                    (1, "Grade 1"),
                    (2, "Grade 2"),
                    (3, "Grade 3"),
                    (4, "Grade 4"),
                    (5, "Grade 5"),
                ],
                null=True,
                verbose_name="Grade",
            ),
        ),
        migrations.AddField(
            model_name="historicalbloodresultsins",
            name="ins_grade_description",
            field=models.CharField(
                blank=True, max_length=250, null=True, verbose_name="Grade description"
            ),
        ),
        migrations.AddField(
            model_name="historicalbloodresultslft",
            name="albumin_quantifier",
            field=models.CharField(
                blank=True,
                choices=[("=", "="), (">", ">"), (">=", ">="), ("<", "<"), ("<=", "<=")],
                default="=",
                max_length=10,
                null=True,
                verbose_name="Quantifier",
            ),
        ),
        migrations.AddField(
            model_name="historicalbloodresultslft",
            name="alp_quantifier",
            field=models.CharField(
                blank=True,
                choices=[("=", "="), (">", ">"), (">=", ">="), ("<", "<"), ("<=", "<=")],
                default="=",
                max_length=10,
                null=True,
                verbose_name="Quantifier",
            ),
        ),
        migrations.AddField(
            model_name="historicalbloodresultslft",
            name="alt_quantifier",
            field=models.CharField(
                blank=True,
                choices=[("=", "="), (">", ">"), (">=", ">="), ("<", "<"), ("<=", "<=")],
                default="=",
                max_length=10,
                null=True,
                verbose_name="Quantifier",
            ),
        ),
        migrations.AddField(
            model_name="historicalbloodresultslft",
            name="amylase_quantifier",
            field=models.CharField(
                blank=True,
                choices=[("=", "="), (">", ">"), (">=", ">="), ("<", "<"), ("<=", "<=")],
                default="=",
                max_length=10,
                null=True,
                verbose_name="Quantifier",
            ),
        ),
        migrations.AddField(
            model_name="historicalbloodresultslft",
            name="ast_quantifier",
            field=models.CharField(
                blank=True,
                choices=[("=", "="), (">", ">"), (">=", ">="), ("<", "<"), ("<=", "<=")],
                default="=",
                max_length=10,
                null=True,
                verbose_name="Quantifier",
            ),
        ),
        migrations.AddField(
            model_name="historicalbloodresultslft",
            name="ggt_quantifier",
            field=models.CharField(
                blank=True,
                choices=[("=", "="), (">", ">"), (">=", ">="), ("<", "<"), ("<=", "<=")],
                default="=",
                max_length=10,
                null=True,
                verbose_name="Quantifier",
            ),
        ),
        migrations.AddField(
            model_name="historicalbloodresultslipid",
            name="chol_quantifier",
            field=models.CharField(
                blank=True,
                choices=[("=", "="), (">", ">"), (">=", ">="), ("<", "<"), ("<=", "<=")],
                default="=",
                max_length=10,
                null=True,
                verbose_name="Quantifier",
            ),
        ),
        migrations.AddField(
            model_name="historicalbloodresultslipid",
            name="hdl_quantifier",
            field=models.CharField(
                blank=True,
                choices=[("=", "="), (">", ">"), (">=", ">="), ("<", "<"), ("<=", "<=")],
                default="=",
                max_length=10,
                null=True,
                verbose_name="Quantifier",
            ),
        ),
        migrations.AddField(
            model_name="historicalbloodresultslipid",
            name="ldl_quantifier",
            field=models.CharField(
                blank=True,
                choices=[("=", "="), (">", ">"), (">=", ">="), ("<", "<"), ("<=", "<=")],
                default="=",
                max_length=10,
                null=True,
                verbose_name="Quantifier",
            ),
        ),
        migrations.AddField(
            model_name="historicalbloodresultslipid",
            name="trig_quantifier",
            field=models.CharField(
                blank=True,
                choices=[("=", "="), (">", ">"), (">=", ">="), ("<", "<"), ("<=", "<=")],
                default="=",
                max_length=10,
                null=True,
                verbose_name="Quantifier",
            ),
        ),
        migrations.AddField(
            model_name="historicalbloodresultsrft",
            name="creatinine_quantifier",
            field=models.CharField(
                blank=True,
                choices=[("=", "="), (">", ">"), (">=", ">="), ("<", "<"), ("<=", "<=")],
                default="=",
                max_length=10,
                null=True,
                verbose_name="Quantifier",
            ),
        ),
        migrations.AddField(
            model_name="historicalbloodresultsrft",
            name="egfr_drop_quantifier",
            field=models.CharField(
                blank=True,
                choices=[("=", "="), (">", ">"), (">=", ">="), ("<", "<"), ("<=", "<=")],
                default="=",
                max_length=10,
                null=True,
                verbose_name="Quantifier",
            ),
        ),
        migrations.AddField(
            model_name="historicalbloodresultsrft",
            name="egfr_quantifier",
            field=models.CharField(
                blank=True,
                choices=[("=", "="), (">", ">"), (">=", ">="), ("<", "<"), ("<=", "<=")],
                default="=",
                max_length=10,
                null=True,
                verbose_name="Quantifier",
            ),
        ),
        migrations.AddField(
            model_name="historicalbloodresultsrft",
            name="urea_quantifier",
            field=models.CharField(
                blank=True,
                choices=[("=", "="), (">", ">"), (">=", ">="), ("<", "<"), ("<=", "<=")],
                default="=",
                max_length=10,
                null=True,
                verbose_name="Quantifier",
            ),
        ),
        migrations.AddField(
            model_name="historicalbloodresultsrft",
            name="uric_acid_quantifier",
            field=models.CharField(
                blank=True,
                choices=[("=", "="), (">", ">"), (">=", ">="), ("<", "<"), ("<=", "<=")],
                default="=",
                max_length=10,
                null=True,
                verbose_name="Quantifier",
            ),
        ),
        migrations.AlterField(
            model_name="bloodresultsins",
            name="ins_quantifier",
            field=models.CharField(
                blank=True,
                choices=[("=", "="), (">", ">"), (">=", ">="), ("<", "<"), ("<=", "<=")],
                default="=",
                max_length=10,
                null=True,
                verbose_name="Quantifier",
            ),
        ),
        migrations.AlterField(
            model_name="bloodresultsins",
            name="ins_units",
            field=models.CharField(
                blank=True,
                choices=[("IU/L", "IU/L")],
                max_length=15,
                null=True,
                verbose_name="units",
            ),
        ),
        migrations.AlterField(
            model_name="bloodresultsins",
            name="ins_value",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=8,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(0.0),
                    django.core.validators.MaxValueValidator(999.0),
                ],
                verbose_name="Insulin",
            ),
        ),
        migrations.AlterField(
            model_name="bloodresultslft",
            name="alp_units",
            field=models.CharField(
                blank=True,
                choices=[("IU/L", "IU/L")],
                max_length=15,
                null=True,
                verbose_name="units",
            ),
        ),
        migrations.AlterField(
            model_name="bloodresultslft",
            name="alt_units",
            field=models.CharField(
                blank=True,
                choices=[("IU/L", "IU/L")],
                max_length=15,
                null=True,
                verbose_name="units",
            ),
        ),
        migrations.AlterField(
            model_name="bloodresultslft",
            name="amylase_units",
            field=models.CharField(
                blank=True,
                choices=[("IU/L", "IU/L")],
                max_length=15,
                null=True,
                verbose_name="units",
            ),
        ),
        migrations.AlterField(
            model_name="bloodresultslft",
            name="ast_units",
            field=models.CharField(
                blank=True,
                choices=[("IU/L", "IU/L")],
                max_length=15,
                null=True,
                verbose_name="units",
            ),
        ),
        migrations.AlterField(
            model_name="bloodresultslft",
            name="ggt_units",
            field=models.CharField(
                blank=True,
                choices=[("IU/L", "IU/L")],
                max_length=15,
                null=True,
                verbose_name="units",
            ),
        ),
        migrations.AlterField(
            model_name="egfrdropnotification",
            name="egfr_percent_change",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                help_text="Copied from RFT result eGFR section.",
                max_digits=10,
                null=True,
                verbose_name="Change from baseline",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbloodresultsins",
            name="ins_quantifier",
            field=models.CharField(
                blank=True,
                choices=[("=", "="), (">", ">"), (">=", ">="), ("<", "<"), ("<=", "<=")],
                default="=",
                max_length=10,
                null=True,
                verbose_name="Quantifier",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbloodresultsins",
            name="ins_units",
            field=models.CharField(
                blank=True,
                choices=[("IU/L", "IU/L")],
                max_length=15,
                null=True,
                verbose_name="units",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbloodresultsins",
            name="ins_value",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=8,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(0.0),
                    django.core.validators.MaxValueValidator(999.0),
                ],
                verbose_name="Insulin",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbloodresultslft",
            name="alp_units",
            field=models.CharField(
                blank=True,
                choices=[("IU/L", "IU/L")],
                max_length=15,
                null=True,
                verbose_name="units",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbloodresultslft",
            name="alt_units",
            field=models.CharField(
                blank=True,
                choices=[("IU/L", "IU/L")],
                max_length=15,
                null=True,
                verbose_name="units",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbloodresultslft",
            name="amylase_units",
            field=models.CharField(
                blank=True,
                choices=[("IU/L", "IU/L")],
                max_length=15,
                null=True,
                verbose_name="units",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbloodresultslft",
            name="ast_units",
            field=models.CharField(
                blank=True,
                choices=[("IU/L", "IU/L")],
                max_length=15,
                null=True,
                verbose_name="units",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbloodresultslft",
            name="ggt_units",
            field=models.CharField(
                blank=True,
                choices=[("IU/L", "IU/L")],
                max_length=15,
                null=True,
                verbose_name="units",
            ),
        ),
        migrations.AlterField(
            model_name="historicalegfrdropnotification",
            name="egfr_percent_change",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                help_text="Copied from RFT result eGFR section.",
                max_digits=10,
                null=True,
                verbose_name="Change from baseline",
            ),
        ),
    ]
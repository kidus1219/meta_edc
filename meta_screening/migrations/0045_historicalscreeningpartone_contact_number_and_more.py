# Generated by Django 4.0.5 on 2022-06-27 14:17

from django.db import migrations
import django_crypto_fields.fields.encrypted_char_field


class Migration(migrations.Migration):
    dependencies = [
        ("meta_screening", "0044_alter_historicalscreeningpartone_severe_htn_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="historicalscreeningpartone",
            name="contact_number",
            field=django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(
                blank=True, help_text=" (Encryption: RSA local)", max_length=71, null=True
            ),
        ),
        migrations.AddField(
            model_name="historicalscreeningpartthree",
            name="contact_number",
            field=django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(
                blank=True, help_text=" (Encryption: RSA local)", max_length=71, null=True
            ),
        ),
        migrations.AddField(
            model_name="historicalscreeningparttwo",
            name="contact_number",
            field=django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(
                blank=True, help_text=" (Encryption: RSA local)", max_length=71, null=True
            ),
        ),
        migrations.AddField(
            model_name="historicalsubjectscreening",
            name="contact_number",
            field=django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(
                blank=True, help_text=" (Encryption: RSA local)", max_length=71, null=True
            ),
        ),
        migrations.AddField(
            model_name="subjectscreening",
            name="contact_number",
            field=django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(
                blank=True, help_text=" (Encryption: RSA local)", max_length=71, null=True
            ),
        ),
    ]

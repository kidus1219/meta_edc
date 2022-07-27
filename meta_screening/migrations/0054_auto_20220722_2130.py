# Generated by Django 3.2.11 on 2022-07-22 18:30

from django.db import migrations, models
import django_crypto_fields.fields.encrypted_char_field


class Migration(migrations.Migration):

    dependencies = [
        ('meta_screening', '0053_auto_20220704_1841'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalscreeningpartone',
            name='aou',
        ),
        migrations.RemoveField(
            model_name='historicalscreeningpartone',
            name='aou_duration',
        ),
        migrations.RemoveField(
            model_name='historicalscreeningpartone',
            name='aou_passed',
        ),
        migrations.RemoveField(
            model_name='historicalscreeningpartthree',
            name='aou',
        ),
        migrations.RemoveField(
            model_name='historicalscreeningpartthree',
            name='aou_duration',
        ),
        migrations.RemoveField(
            model_name='historicalscreeningpartthree',
            name='aou_passed',
        ),
        migrations.RemoveField(
            model_name='historicalscreeningparttwo',
            name='aou',
        ),
        migrations.RemoveField(
            model_name='historicalscreeningparttwo',
            name='aou_duration',
        ),
        migrations.RemoveField(
            model_name='historicalscreeningparttwo',
            name='aou_passed',
        ),
        migrations.RemoveField(
            model_name='historicalsubjectscreening',
            name='aou',
        ),
        migrations.RemoveField(
            model_name='historicalsubjectscreening',
            name='aou_duration',
        ),
        migrations.RemoveField(
            model_name='historicalsubjectscreening',
            name='aou_passed',
        ),
        migrations.RemoveField(
            model_name='subjectscreening',
            name='aou',
        ),
        migrations.RemoveField(
            model_name='subjectscreening',
            name='aou_duration',
        ),
        migrations.RemoveField(
            model_name='subjectscreening',
            name='aou_passed',
        ),
        migrations.AddField(
            model_name='historicalicpreferral',
            name='referred_datetime',
            field=models.DateTimeField(help_text='Date and time of referral', null=True),
        ),
        migrations.AddField(
            model_name='icpreferral',
            name='referred_datetime',
            field=models.DateTimeField(help_text='Date and time of referral', null=True),
        ),
        migrations.AlterField(
            model_name='historicalicpreferral',
            name='hospital_identifier',
            field=django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(blank=True, help_text=' (Encryption: RSA local)', max_length=71, null=True),
        ),
        migrations.AlterField(
            model_name='historicalicpreferral',
            name='referred',
            field=models.BooleanField(default=False, verbose_name='Referred'),
        ),
        migrations.AlterField(
            model_name='historicalscreeningpartone',
            name='staying_nearby_6',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], editable=False, help_text='META PHASE_TWO ONLY', max_length=15, null=True, verbose_name='Is the patient planning to remain in the catchment area for at least 6 months'),
        ),
        migrations.AlterField(
            model_name='historicalscreeningpartthree',
            name='staying_nearby_6',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], editable=False, help_text='META PHASE_TWO ONLY', max_length=15, null=True, verbose_name='Is the patient planning to remain in the catchment area for at least 6 months'),
        ),
        migrations.AlterField(
            model_name='historicalscreeningparttwo',
            name='staying_nearby_6',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], editable=False, help_text='META PHASE_TWO ONLY', max_length=15, null=True, verbose_name='Is the patient planning to remain in the catchment area for at least 6 months'),
        ),
        migrations.AlterField(
            model_name='historicalsubjectscreening',
            name='staying_nearby_6',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], editable=False, help_text='META PHASE_TWO ONLY', max_length=15, null=True, verbose_name='Is the patient planning to remain in the catchment area for at least 6 months'),
        ),
        migrations.AlterField(
            model_name='icpreferral',
            name='hospital_identifier',
            field=django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(blank=True, help_text=' (Encryption: RSA local)', max_length=71, null=True),
        ),
        migrations.AlterField(
            model_name='icpreferral',
            name='referred',
            field=models.BooleanField(default=False, verbose_name='Referred'),
        ),
        migrations.AlterField(
            model_name='subjectscreening',
            name='staying_nearby_6',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], editable=False, help_text='META PHASE_TWO ONLY', max_length=15, null=True, verbose_name='Is the patient planning to remain in the catchment area for at least 6 months'),
        ),
    ]

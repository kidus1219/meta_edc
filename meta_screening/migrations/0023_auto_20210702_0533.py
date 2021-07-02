# Generated by Django 3.2.4 on 2021-07-02 02:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meta_screening', '0022_auto_20210702_0426'),
    ]

    operations = [
        migrations.RenameField(
            model_name='historicalscreeningpartone',
            old_name='fasted',
            new_name='fasting',
        ),
        migrations.RenameField(
            model_name='historicalscreeningpartone',
            old_name='fasted_duration_minutes',
            new_name='fasting_duration_minutes',
        ),
        migrations.RenameField(
            model_name='historicalscreeningpartone',
            old_name='fasted_duration_str',
            new_name='fasting_duration_str',
        ),
        migrations.RenameField(
            model_name='historicalscreeningpartthree',
            old_name='fasted',
            new_name='fasting',
        ),
        migrations.RenameField(
            model_name='historicalscreeningpartthree',
            old_name='fasted_duration_minutes',
            new_name='fasting_duration_minutes',
        ),
        migrations.RenameField(
            model_name='historicalscreeningpartthree',
            old_name='fasted_duration_str',
            new_name='fasting_duration_str',
        ),
        migrations.RenameField(
            model_name='historicalscreeningparttwo',
            old_name='fasted',
            new_name='fasting',
        ),
        migrations.RenameField(
            model_name='historicalscreeningparttwo',
            old_name='fasted_duration_minutes',
            new_name='fasting_duration_minutes',
        ),
        migrations.RenameField(
            model_name='historicalscreeningparttwo',
            old_name='fasted_duration_str',
            new_name='fasting_duration_str',
        ),
        migrations.RenameField(
            model_name='historicalsubjectscreening',
            old_name='fasted',
            new_name='fasting',
        ),
        migrations.RenameField(
            model_name='historicalsubjectscreening',
            old_name='fasted_duration_minutes',
            new_name='fasting_duration_minutes',
        ),
        migrations.RenameField(
            model_name='historicalsubjectscreening',
            old_name='fasted_duration_str',
            new_name='fasting_duration_str',
        ),
        migrations.RenameField(
            model_name='subjectscreening',
            old_name='fasted',
            new_name='fasting',
        ),
        migrations.RenameField(
            model_name='subjectscreening',
            old_name='fasted_duration_minutes',
            new_name='fasting_duration_minutes',
        ),
        migrations.RenameField(
            model_name='subjectscreening',
            old_name='fasted_duration_str',
            new_name='fasting_duration_str',
        ),
    ]
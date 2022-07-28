# Generated by Django 3.2.11 on 2022-07-19 18:34

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("sites", "0002_alter_domain_unique"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("edc_action_item", "0029_auto_20220704_1841"),
        ("meta_subject", "0124_auto_20220714_2303"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="EgfrNotification",
            new_name="EgfrDropNotification",
        ),
        migrations.RenameModel(
            old_name="HistoricalEgfrNotification",
            new_name="HistoricalEgfrDropNotification",
        ),
        migrations.AlterModelOptions(
            name="egfrdropnotification",
            options={
                "default_permissions": ("add", "change", "delete", "view", "export", "import"),
                "get_latest_by": "modified",
                "ordering": ("-modified", "-created"),
                "verbose_name": "eGFR Drop Notification",
                "verbose_name_plural": "eGFR Drop Notifications",
            },
        ),
        migrations.AlterModelOptions(
            name="historicalegfrdropnotification",
            options={
                "get_latest_by": ("history_date", "history_id"),
                "ordering": ("-history_date", "-history_id"),
                "verbose_name": "historical eGFR Drop Notification",
                "verbose_name_plural": "historical eGFR Drop Notifications",
            },
        ),
    ]

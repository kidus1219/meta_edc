# Generated by Django 4.0.5 on 2022-07-03 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meta_lists', '0012_auto_20210728_1809'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransferReasons',
            fields=[
                ('name', models.CharField(db_index=True, help_text='This is the stored value, required', max_length=250, unique=True, verbose_name='Stored value')),
                ('display_name', models.CharField(db_index=True, help_text='(suggest 40 characters max.)', max_length=250, unique=True, verbose_name='Name')),
                ('display_index', models.IntegerField(db_index=True, default=0, help_text='Index to control display order if not alphabetical, not required', verbose_name='display index')),
                ('field_name', models.CharField(blank=True, editable=False, help_text='Not required', max_length=25, null=True)),
                ('version', models.CharField(default='1.0', editable=False, max_length=35)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Transfer Reasons',
                'verbose_name_plural': 'Transfer Reasons',
                'ordering': ['display_index', 'display_name'],
                'abstract': False,
                'default_permissions': ('add', 'change', 'delete', 'view', 'export', 'import'),
            },
        ),
        migrations.AddIndex(
            model_name='transferreasons',
            index=models.Index(fields=['id', 'display_name', 'display_index'], name='meta_lists__id_77e6e7_idx'),
        ),
    ]

# Generated by Django 2.2.7 on 2019-11-06 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20191106_1639'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='ptub_date',
            new_name='prtub_date',
        ),
    ]

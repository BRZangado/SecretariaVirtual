# Generated by Django 2.0.7 on 2018-08-10 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_solicitation_document'),
    ]

    operations = [
        migrations.RenameField(
            model_name='solicitation',
            old_name='document',
            new_name='attachment',
        ),
    ]
# Generated by Django 4.0.8 on 2023-01-21 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_usercomfirmation_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usercomfirmation',
            old_name='is_conformed',
            new_name='is_confirmed',
        ),
    ]

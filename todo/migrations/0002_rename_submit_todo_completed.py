# Generated by Django 3.2 on 2024-12-24 07:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='submit',
            new_name='completed',
        ),
    ]

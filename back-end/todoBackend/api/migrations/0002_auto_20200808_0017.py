# Generated by Django 3.1 on 2020-08-07 18:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todomodel',
            old_name='titie',
            new_name='title',
        ),
    ]
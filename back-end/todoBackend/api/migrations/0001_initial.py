# Generated by Django 3.1 on 2020-08-07 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titie', models.CharField(max_length=250)),
                ('completed', models.BooleanField(blank=True, default=False)),
                ('scheduled', models.BooleanField(blank=True, default=False)),
                ('time', models.TimeField()),
            ],
        ),
    ]

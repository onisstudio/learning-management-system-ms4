# Generated by Django 3.0.6 on 2020-06-04 22:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_auto_20200604_2124'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, editable=False),
        ),
        migrations.AddField(
            model_name='course',
            name='updated',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]

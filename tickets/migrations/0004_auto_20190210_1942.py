# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-02-11 00:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0003_auto_20190210_1052'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='title',
            field=models.CharField(default='Fake Title', max_length=80),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='followup',
            name='action',
            field=models.CharField(choices=[('closed', 'Closed'), ('re-opened', 'Re-Opened'), ('split', 'Split'), ('no_action', 'No Action')], default='no_action', max_length=20),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='priority',
            field=models.IntegerField(choices=[(3, 'Normal'), (2, 'High'), (5, 'Very Low'), (4, 'Low'), (1, 'Critical')]),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=models.CharField(choices=[('re-opened', 'Re-Opened'), ('closed', 'Closed'), ('assigned', 'Assigned'), ('new', 'New'), ('duplicate', 'Closed - Duplicate'), ('split', 'Closed - Split'), ('accepted', 'Accepted')], default=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='ticket_type',
            field=models.CharField(choices=[('feature', 'Feature Request'), ('bug', 'Bug Report'), ('task', 'Task')], default=True, max_length=10),
        ),
    ]

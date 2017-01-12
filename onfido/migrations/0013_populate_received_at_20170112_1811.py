# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-12 18:11
from __future__ import unicode_literals

from django.db import migrations


def set_event_received_at(apps, schema_editor):
    Event = apps.get_model("onfido", "Event")
    for event in Event.objects.all():
        event.received_at = event.completed_at
        event.save()


class Migration(migrations.Migration):

    dependencies = [
        ('onfido', '0012_add_event_received_at_timestamp'),
    ]

    operations = [
        migrations.RunPython(set_event_received_at),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2020-03-20 19:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("proposals", "0024_auto_20170610_1857"),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name="proposalcomment",
            index_together=set(
                [("is_spam", "marked_as_spam_by"), ("commenter", "is_spam")]
            ),
        ),
    ]
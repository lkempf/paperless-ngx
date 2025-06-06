# Generated by Django 5.1.8 on 2025-05-23 05:50

import datetime

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [
        ("documents", "1067_alter_document_created"),
    ]

    operations = [
        migrations.AlterField(
            model_name="document",
            name="created",
            field=models.DateField(
                db_index=True,
                default=datetime.date.today,
                verbose_name="created",
            ),
        ),
    ]

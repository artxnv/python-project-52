# Generated by Django 4.2.16 on 2024-11-01 12:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("statuses", "0001_initial"),
        ("tasks", "0003_alter_task_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="status",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="tasks",
                to="statuses.status",
                verbose_name="Status",
            ),
        ),
    ]

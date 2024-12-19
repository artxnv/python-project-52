# Generated by Django 4.2.16 on 2024-11-01 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("statuses", "0001_initial"),
        ("tasks", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="status",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="status",
                to="statuses.status",
                verbose_name="Status",
            ),
        ),
    ]

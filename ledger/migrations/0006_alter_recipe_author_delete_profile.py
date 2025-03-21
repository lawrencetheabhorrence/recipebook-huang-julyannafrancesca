# Generated by Django 5.1.6 on 2025-03-17 01:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ledger", "0005_auto_20250316_0317"),
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipe",
            name="author",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="user.profile",
            ),
        ),
        migrations.DeleteModel(
            name="Profile",
        ),
    ]

# Generated by Django 4.1.5 on 2023-01-28 22:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="User",
            new_name="Account",
        ),
    ]

# Generated by Django 4.1.2 on 2022-10-31 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app_assignment", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="submission",
            old_name="instruction",
            new_name="description",
        ),
    ]

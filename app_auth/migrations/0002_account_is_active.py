# Generated by Django 4.0.5 on 2022-07-22 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_auth", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="account",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
    ]
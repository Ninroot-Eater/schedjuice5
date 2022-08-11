# Generated by Django 4.0.5 on 2022-08-11 08:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("app_auth", "0004_remove_account_groups_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="account",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="account",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
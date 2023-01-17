# Generated by Django 4.1.2 on 2023-01-17 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_auth", "0006_alter_tempemail_account"),
    ]

    operations = [
        migrations.AlterField(
            model_name="account",
            name="email",
            field=models.EmailField(
                error_messages={"blank": {"default": "This field is required."}},
                help_text="The user's email address ending in the organisation's domain.",
                max_length=254,
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="account",
            name="is_staff",
            field=models.BooleanField(default=True),
        ),
    ]

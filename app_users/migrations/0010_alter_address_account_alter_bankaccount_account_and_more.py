# Generated by Django 4.1.2 on 2022-12-13 13:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("app_users", "0009_alter_address_account_alter_bankaccount_account"),
    ]

    operations = [
        migrations.AlterField(
            model_name="address",
            name="account",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="addresses",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="bankaccount",
            name="account",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="bank_accounts",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="phonenumber",
            name="account",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="phone_numbers",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]

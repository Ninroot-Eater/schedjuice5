# Generated by Django 4.1.2 on 2022-12-13 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app_users", "0010_alter_address_account_alter_bankaccount_account_and_more"),
        ("app_announcement", "0002_attachment"),
    ]

    operations = [
        migrations.AlterField(
            model_name="announcement",
            name="created_by",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="announcements",
                to="app_users.staff",
            ),
        ),
        migrations.AlterField(
            model_name="attachment",
            name="announcement",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="attachments",
                to="app_announcement.announcement",
            ),
        ),
    ]
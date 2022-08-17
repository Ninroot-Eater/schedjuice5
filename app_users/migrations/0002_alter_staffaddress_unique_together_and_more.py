# Generated by Django 4.0.5 on 2022-08-16 13:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='staffaddress',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='staffbankaccount',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='studentaddress',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='studentbankaccount',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='staffaddress',
            name='is_primary',
            field=models.BooleanField(default=False, help_text='A flag for whether current Address is a primary one or not.'),
        ),
        migrations.AlterField(
            model_name='staffaddress',
            name='save_name',
            field=models.CharField(help_text='The name to save the current Address as.', max_length=256, validators=[django.core.validators.RegexValidator(message="Field must match this: '[a-zA-Z0-9_\\-\\(\\) ]'", regex='[a-zA-Z0-9_\\-\\(\\) ]')]),
        ),
        migrations.AlterField(
            model_name='staffbankaccount',
            name='is_primary',
            field=models.BooleanField(default=False, help_text='A flag for whether current BankAccount is a primary one or not.'),
        ),
        migrations.AlterField(
            model_name='staffbankaccount',
            name='save_name',
            field=models.CharField(help_text='The name to save the current BankAccount as.', max_length=256, validators=[django.core.validators.RegexValidator(message="Field must match this: '[a-zA-Z0-9_\\-\\(\\) ]'", regex='[a-zA-Z0-9_\\-\\(\\) ]')]),
        ),
        migrations.AlterField(
            model_name='studentaddress',
            name='is_primary',
            field=models.BooleanField(default=False, help_text='A flag for whether current Address is a primary one or not.'),
        ),
        migrations.AlterField(
            model_name='studentaddress',
            name='save_name',
            field=models.CharField(help_text='The name to save the current Address as.', max_length=256, validators=[django.core.validators.RegexValidator(message="Field must match this: '[a-zA-Z0-9_\\-\\(\\) ]'", regex='[a-zA-Z0-9_\\-\\(\\) ]')]),
        ),
        migrations.AlterField(
            model_name='studentbankaccount',
            name='is_primary',
            field=models.BooleanField(default=False, help_text='A flag for whether current BankAccount is a primary one or not.'),
        ),
        migrations.AlterField(
            model_name='studentbankaccount',
            name='save_name',
            field=models.CharField(help_text='The name to save the current BankAccount as.', max_length=256, validators=[django.core.validators.RegexValidator(message="Field must match this: '[a-zA-Z0-9_\\-\\(\\) ]'", regex='[a-zA-Z0-9_\\-\\(\\) ]')]),
        ),
        migrations.AlterUniqueTogether(
            name='staffaddress',
            unique_together={('staff', 'address', 'save_name')},
        ),
        migrations.AlterUniqueTogether(
            name='staffbankaccount',
            unique_together={('staff', 'bank_account', 'save_name')},
        ),
        migrations.AlterUniqueTogether(
            name='studentaddress',
            unique_together={('student', 'address', 'save_name')},
        ),
        migrations.AlterUniqueTogether(
            name='studentbankaccount',
            unique_together={('student', 'bank_account', 'save_name')},
        ),
    ]
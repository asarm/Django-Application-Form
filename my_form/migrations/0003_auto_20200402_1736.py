# Generated by Django 3.0.4 on 2020-04-02 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_form', '0002_remove_applicant_available_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='applicant',
            old_name='linkedIn',
            new_name='linkedin',
        ),
        migrations.RenameField(
            model_name='applicant',
            old_name='phone_number',
            new_name='number',
        ),
    ]
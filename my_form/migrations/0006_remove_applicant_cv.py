# Generated by Django 3.0.4 on 2020-04-02 18:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_form', '0005_auto_20200402_2122'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applicant',
            name='cv',
        ),
    ]

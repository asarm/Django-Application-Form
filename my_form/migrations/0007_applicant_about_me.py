# Generated by Django 3.0.4 on 2020-04-02 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_form', '0006_remove_applicant_cv'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicant',
            name='about_me',
            field=models.TextField(default='About Me', max_length=500),
        ),
    ]

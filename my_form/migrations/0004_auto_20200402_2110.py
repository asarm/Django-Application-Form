# Generated by Django 3.0.4 on 2020-04-02 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_form', '0003_auto_20200402_1736'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicant',
            name='cv',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='github',
            field=models.URLField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='linkedin',
            field=models.URLField(default='', max_length=150),
        ),
    ]

# Generated by Django 2.2.4 on 2019-10-29 10:49

import HelpMePickApp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HelpMePickApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='pict',
            field=models.ImageField(blank=True, null=True, upload_to=HelpMePickApp.models.get_image_path),
        ),
    ]
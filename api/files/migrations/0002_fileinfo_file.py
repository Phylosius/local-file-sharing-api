# Generated by Django 5.1.3 on 2024-11-18 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fileinfo',
            name='file',
            field=models.FileField(null=True, upload_to='public'),
        ),
    ]

# Generated by Django 3.0.6 on 2020-06-05 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0009_auto_20200605_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='image',
            field=models.ImageField(upload_to='user_images'),
        ),
        migrations.AlterField(
            model_name='roomname',
            name='image',
            field=models.ImageField(upload_to='roomName_images'),
        ),
    ]

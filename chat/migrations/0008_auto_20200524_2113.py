# Generated by Django 3.0.6 on 2020-05-24 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0007_roomname_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roomname',
            name='person',
            field=models.ManyToManyField(to='chat.person'),
        ),
    ]

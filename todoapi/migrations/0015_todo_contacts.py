# Generated by Django 4.1.7 on 2023-03-08 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapi', '0014_contact_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='contacts',
            field=models.ManyToManyField(to='todoapi.contact'),
        ),
    ]

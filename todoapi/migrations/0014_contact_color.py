# Generated by Django 4.1.7 on 2023-03-06 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapi', '0013_alter_todo_name_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='color',
            field=models.CharField(default=None, max_length=20),
        ),
    ]

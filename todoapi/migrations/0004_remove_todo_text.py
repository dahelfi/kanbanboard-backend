# Generated by Django 4.1.7 on 2023-02-26 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapi', '0003_alter_todo_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='text',
        ),
    ]

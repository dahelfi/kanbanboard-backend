# Generated by Django 4.1.7 on 2023-02-26 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapi', '0004_remove_todo_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='category',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AddField(
            model_name='todo',
            name='desrcription',
            field=models.TextField(default=None, max_length=500),
        ),
        migrations.AddField(
            model_name='todo',
            name='name',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AddField(
            model_name='todo',
            name='priority',
            field=models.CharField(default=None, max_length=20),
        ),
    ]
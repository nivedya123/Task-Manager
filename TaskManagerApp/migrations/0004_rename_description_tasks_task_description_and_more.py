# Generated by Django 5.1.3 on 2024-11-18 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TaskManagerApp', '0003_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tasks',
            old_name='description',
            new_name='task_description',
        ),
        migrations.RenameField(
            model_name='tasks',
            old_name='title',
            new_name='task_name',
        ),
        migrations.RemoveField(
            model_name='tasks',
            name='created_time',
        ),
    ]

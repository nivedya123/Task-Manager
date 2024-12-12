# Generated by Django 5.1.3 on 2024-11-19 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TaskManagerApp', '0004_rename_description_tasks_task_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('task_id', models.AutoField(primary_key=True, serialize=False)),
                ('task_name', models.CharField(max_length=255)),
                ('task_description', models.TextField(blank=True, null=True)),
                ('total_effort', models.IntegerField()),
                ('status', models.CharField(choices=[('need to do', 'Need to do'), ('in progress', 'In progress'), ('on hold', 'On hold'), ('completed', 'Completed')], default='need to do', max_length=50)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Tasks',
        ),
    ]

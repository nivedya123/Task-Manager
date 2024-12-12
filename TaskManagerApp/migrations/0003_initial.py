# Generated by Django 5.1.3 on 2024-11-18 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('TaskManagerApp', '0002_delete_tasks'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('total_effort', models.IntegerField()),
                ('status', models.CharField(choices=[('need to start', 'need to start'), ('in progress', 'in progress'), ('on hold', 'on hold'), ('completed', 'completed')], default='need to start', max_length=20)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
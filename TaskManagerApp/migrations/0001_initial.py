# Generated by Django 5.1.3 on 2024-11-15 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('total_effort', models.IntegerField()),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Need to Start', 'Need to Start'), ('In Progress', 'In Progress'), ('On Hold', 'On Hold'), ('Completed', 'Completed')], default='Need to Start', max_length=20)),
            ],
        ),
    ]

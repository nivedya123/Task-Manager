from django.db import models

#django model for Task table
class Task(models.Model):
    STATUS_CHOICES = [
        ('need to do', 'Need to do'),
        ('in progress', 'In progress'),
        ('on hold', 'On hold'),
        ('completed', 'Completed'),
    ]

    task_id = models.AutoField(primary_key=True)
    task_name = models.CharField(max_length=255)
    task_description = models.TextField(blank=True, null=True)
    total_effort = models.IntegerField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='need to do')
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task_name
from django import forms
from .models import Task

class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_name', 'task_description', 'total_effort', 'status']


class UpdateTaskForm(forms.ModelForm):
     task = forms.ModelChoiceField(
        queryset=Task.objects.all(),
        label='Select Task to Update',
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Select Task to Update"
    )
     class Meta:
        model = Task
        fields = ['task_name', 'task_description', 'total_effort', 'status']


class DeleteTaskForm(forms.Form):
    task = forms.ModelChoiceField(queryset=Task.objects.all(), label="Select Task to Remove",widget=forms.Select(attrs={'class': 'styled-select'}), empty_label="Select an item")

       
    
    
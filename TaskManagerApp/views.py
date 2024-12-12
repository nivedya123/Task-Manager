from django.shortcuts import render,redirect,get_list_or_404,get_object_or_404
from .models import Task
from .forms import *
from django.contrib import messages
from django.http import JsonResponse,HttpResponse



#Displaying the task list as category basis
def task_list(request):
    return render(request,'TaskManagerApp/task_list.html')


#Task updation
def edit_task(request):
    if request.method == 'POST':
        if 'select_task' in request.POST:
            task_id = request.POST.get('task')
            task = get_object_or_404(Task, task_id=task_id)
            form = UpdateTaskForm(instance=task)
        else:
            task_id = request.POST.get('task')
            task = get_object_or_404(Task, task_id=task_id)
            form = UpdateTaskForm(request.POST, instance=task)
            if form.is_valid():
                form.save()
                return redirect('task_list')  # Redirect to a task list or another page after updating
    else:
        form = UpdateTaskForm()

    return render(request, 'TaskManagerApp/edit_task.html', {'form': form})


#Task deletion in task id basis
def remove_task(request):
    if request.method == 'POST':
        form = DeleteTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data['task']
            task.delete()
            return redirect('remove_task')  # Redirect to the task list view after deletion
        return HttpResponse("Invalid form submission", status=400)
    else:
        form = DeleteTaskForm()
    
    tasks = Task.objects.all()
    return render(request, 'TaskManagerApp/remove_task.html', {'form': form, 'tasks': tasks})




















def view_tasks(request,status):
    tasks = Task.objects.filter(status = status)
    return render(request, 'TaskManagerApp/view_task.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        form = AddTaskForm(request.POST)
        delete_task_id = request.POST.get('delete_task')
        if delete_task_id:
            try:
                task_to_delete = Task.objects.get(id=delete_task_id)
                task_to_delete.delete()
            except Task.DoesNotExist:
                messages.error(request,"no task")
        if 'task_name' in request.POST:
           if form.is_valid():
               form.save()
               messages.success(request,"Task Successfully Saved")
               return redirect('add_task')
    else:
        form = AddTaskForm()
    tasks = Task.objects.all()
    return render(request,'TaskManagerApp/add_task.html',{'form':form,'tasks':tasks})

        
    
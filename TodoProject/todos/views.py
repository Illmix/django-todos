from django.http import HttpRequest
from django.shortcuts import render, redirect
from .models import Todo


# Create your views here.
def list_todo_function(request):
    context = {'todo_list': Todo.objects.all()}
    return render(request, 'todos/todo_list.html', context)


def insert_todo_item(request: HttpRequest):
    todo = Todo(content=request.POST['content'])
    todo.save()
    return redirect('/todos/list')


def delete_todo_item(request, todo_id):
    todo_to_delete = Todo.objects.get(id=todo_id)
    todo_to_delete.delete()
    return redirect('/todos/list')


def page_not_found_view(request):
    return redirect('/todos/list/')

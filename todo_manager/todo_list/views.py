from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import ToDoItem


def index_view(request: HttpRequest) -> HttpResponse:
    todo_items = ToDoItem.objects.all()
    return render(request, 'todo_list/index.html', context={'todo_items': todo_items})

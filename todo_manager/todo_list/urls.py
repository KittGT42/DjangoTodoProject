from django.urls import path

from .views import TodoListIndexView, ToDoListView, ToDoListDoneView, ToDoDetailView

app_name = 'todo_list'

urlpatterns = [
    path('<int:pk>/', ToDoDetailView.as_view(), name='detail'),
    path('', TodoListIndexView.as_view(), name='index'),
    path('list/', ToDoListView.as_view(), name='list'),
    path('done/', ToDoListDoneView.as_view(), name='done'),

]

from django.urls import path

from .views import TodoView, TaskUpdateView, TaskDeleteView, CheckView
urlpatterns = [
    path("", TodoView.as_view(), name="todo-list"),
    path("<int:pk>/edit/", TaskUpdateView.as_view(), name="update-todo"),
    path("<int:pk>/delete/", TaskDeleteView.as_view(), name="delete-todo"),
    path("<int:pk>/check/", CheckView, name="check-todo"),
]

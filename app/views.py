from django.views import View
from .models import Task
from .forms import *

# Create your views here.

class TodoView(View):
    form_class = TaskForm
    template_name = "app/index.html"

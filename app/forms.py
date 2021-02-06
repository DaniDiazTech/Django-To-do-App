from django.forms import ModelForm
from django import forms

from .models import Task


class TaskForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control my-2", "placeholder": "The title of the task"}))

    class Meta:
        model = Task
        fields = ('name',)

class TaskUpdateForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control my-2", "placeholder": "The title of the task"}))

    description = forms.CharField(widget=forms.Textarea(
        attrs={"class": "form-control my-2", "placeholder": "The Description of the task"}))

    class Meta:
        model = Task
        fields = ('name', 'description')

class TaskUpdateCheckForm(forms.ModelForm):

    complete = forms.CheckboxInput(attrs={"class": "form-check-input"})

    class Meta:
        model = Task
        fields = ('complete',)

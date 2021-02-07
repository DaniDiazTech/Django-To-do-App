from django.forms import ModelForm
from django import forms

from .models import Task


class TaskForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control form-control-lg", "placeholder": "Task title"}))

    class Meta:
        model = Task
        fields = ('name',)


class TaskUpdateForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control ", "placeholder": "The title of the task"}))

    description = forms.CharField(required=False, widget=forms.Textarea(
        attrs={"class": "form-control ", "placeholder": "The Description of the task"}))

    complete = forms.CharField(required=False, widget=forms.CheckboxInput(
        attrs={"class": "form-check-input"}))

    class Meta:
        model = Task
        fields = ('name', 'description', 'complete')


class TaskUpdateCheckForm(forms.ModelForm):

    complete = forms.CharField(widget=forms.CheckboxInput(
        attrs={"class": "form-check-input"}))

    class Meta:
        model = Task
        fields = ('complete',)

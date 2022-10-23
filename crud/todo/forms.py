from dataclasses import fields
from socket import fromshare
from django import forms
from .models import Tarea

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['tarea','status']
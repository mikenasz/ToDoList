from django import forms
from .models import todo


class TaskForm(forms.ModelForm):
    class Meta:
        model = todo
        fields = '__all__'
        widgets = {
            'task_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Add tasks"
            }),
            'completed': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                'role': "switch"
            })

        }




from .models import Employee
from django import forms

class UpdateForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"
        
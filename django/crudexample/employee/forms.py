from django import forms
from employee.models import Employee


class EmployeeForms(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"
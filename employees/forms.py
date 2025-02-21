from django import forms
from .models import Department, Floor, Salary,  Position, Employee

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ["name", 'description']
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Department"}),
            "description": forms.TextInput(attrs={"class": "form-control", "placeholder": "Department"})
        }

        help_texts = {
            "name": "Please enter a unique department name.",
            "description": "Please provide a brief description of the department.",
        }

class FloorForm(forms.ModelForm):
    class Meta:
        model = Floor
        fields = ["name"]

        labels = {
            "name": "Floor",
        }

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Floor"}),
        }

        help_texts = {
            "name": "Please enter a unique floor name.",
        }
        error_messages = {
            "name": {"unique": "A floor with this name already exists."},
        }


class SalaryForm(forms.ModelForm):
    class Meta:
        model = Salary
        fields = ["amount"]
        labels = {
            "amount": "Salary",
        }
        widgets = {
            "amount": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Salary"}),
        }
        help_texts = {
            "amount": "Please enter the monthly salary amount.",
        }
        error_messages = {
            "amount": {"min_value": "Salary amount must be a positive number."},
        }

        def clean_amount(self):
            amount = self.cleaned_data.get("amount")
            if amount < 0:
                raise forms.ValidationError("Salary amount must be a positive number.")
            return amount
        
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ["employee_id","name", 'join_date', 'date_of_birth', 'floor', 'department', 'position', 'salary']

        labels = {

            "employee_id": 'ID',
            "name": "Name",
            "join_date": "Join Date",
            "date_of_birth": "Date of Birth",
            "floor": "Floor",
            "department": "Department",
            "position": "Position",
            "salary": "Salary",
        }


        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Name"}),
            "join_date": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "date_of_birth": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "floor": forms.Select(attrs={"class": "form-control"}),
            "department": forms.Select(attrs={"class": "form-control"}),
            "position": forms.Select(attrs={"class": "form-control"}),
            "salary": forms.Select(attrs={"class": "form-control"}),
        }
        


from django.shortcuts import render, get_object_or_404, redirect
from .models import Department, Floor, Position, Salary, Employee
from django.contrib import messages
from .forms import EmployeeForm
from django.contrib.auth.decorators import login_required


# Our All Employees 

def employee_all(request):
    employees = Employee.objects.all()
    return render(request, 'employees/all.html', {'employees': employees})

# List all employees
def employee_view(request):
    employees = Employee.objects.all()
    return render(request, 'employees/list.html', {'employees': employees})

# Employee detail view
def employee_detail(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    return render(request, 'employees/detail.html', {'employee': employee})

# Add new employee
@login_required
def employee_add(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save()
            messages.success(request, "Employee added successfully!")
            return redirect('employee_detail', employee_id=employee.id)
    else:
        form = EmployeeForm()
    return render(request, 'employees/add.html', {'form': form})

# Edit employee
@login_required
def employee_edit(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            messages.success(request, "Employee updated successfully!")
            return redirect('employee_detail', employee_id=employee.id)
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employees/edit.html', {'form': form})

# Delete employee
@login_required
def employee_delete(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    if request.method == "POST":
        employee.delete()
        messages.success(request, "Employee deleted successfully!")
        return redirect("employee_view")
    return render(request, 'employees/delete.html', {'employee': employee})

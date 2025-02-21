from django.db import models 
from django.contrib.auth.models import User

class Floor(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Salary(models.Model):
    GRADE_CHOICES = [
        ('A', 'Grade A'),
        ('B', 'Grade B'),
        ('C', 'Grade C'),
        ('D', 'Grade D'),
    ]
    
    grade = models.CharField(max_length=1, choices=GRADE_CHOICES, unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.get_grade_display()} - ${self.amount}"

class Position(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    employee_id = models.CharField(max_length=20)
    name = models.CharField(max_length=255)
    join_date = models.DateField()
    date_of_birth = models.DateField()
    floor = models.ForeignKey(Floor, on_delete=models.SET_NULL, null=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True)
    salary = models.ForeignKey(Salary, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.employee_id} - {self.name}"

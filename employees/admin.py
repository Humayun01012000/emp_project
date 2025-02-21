from django.contrib import admin 
from .models import Floor, Department, Position, Employee, Salary

# Register your models here.
admin.site.register(Floor)
admin.site.register(Department)
admin.site.register(Position)
admin.site.register(Employee)
admin.site.register(Salary)
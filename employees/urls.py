from django.urls import path
from . import views

urlpatterns = [
    path("", views.employee_all, name = "employees"),
    path("employees/", views.employee_view, name="employee_view"),
    path("employee/<int:employee_id>/", views.employee_detail, name="employee_detail"),
    path("employee/add/", views.employee_add, name="employee_add"),
    path("employee/edit/<int:employee_id>/", views.employee_edit, name="employee_edit"),
    path("employee/delete/<int:employee_id>/", views.employee_delete, name="employee_delete"),
]

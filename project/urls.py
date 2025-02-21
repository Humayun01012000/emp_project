
from django.contrib import admin
from django.urls import path, include


urlpatterns =[
    path("admin/", admin.site.urls),
    path("", include("employees.urls")),
    path("attendance/", include("attendance.urls")),
    path("auth", include("authentication.urls")),
]
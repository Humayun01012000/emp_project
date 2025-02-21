from django.urls import path
from .views import (
    ShiftListView, ShiftCreateView, ShiftUpdateView, ShiftDeleteView,
    ShiftScheduleListView, ShiftScheduleCreateView, ShiftScheduleUpdateView, ShiftScheduleDeleteView,

    ShiftReportListView, ShiftReportCreateView, ShiftReportUpdateView, ShiftReportDeleteView,
    ShiftReportDetailView, create_shift_report_detail,delete_shift_report_detail,
    LeaveRequestListView, LeaveRequestCreateView, LeaveRequestUpdateView, LeaveRequestDeleteView,
    attendance_list, attendance_create,attendance_update,attendance_report,attendance_delete
    
)
urlpatterns = [
    # Shift URLs
    path('shifts/', ShiftListView.as_view(), name='shift_list'),
    path('shifts/new/', ShiftCreateView.as_view(), name='shift_create'),
    path('shifts/edit/<int:pk>/', ShiftUpdateView.as_view(), name='shift_edit'),
    path('shifts/delete/<int:pk>/', ShiftDeleteView.as_view(), name='shift_delete'),

    # Shift Schedule URLs
    path('schedules/', ShiftScheduleListView.as_view(), name='schedule_list'),
    path('schedules/new/', ShiftScheduleCreateView.as_view(), name='schedule_create'),
    path('schedules/edit/<int:pk>/', ShiftScheduleUpdateView.as_view(), name='schedule_edit'),
    path('schedules/delete/<int:pk>/', ShiftScheduleDeleteView.as_view(), name='schedule_delete'),

    # Shift Report URLs


    path('reports/', ShiftReportListView.as_view(), name='report_list'),
    path('reports/new/', ShiftReportCreateView.as_view(), name='report_create'),
    path('reports/<int:pk>/', ShiftReportDetailView.as_view(), name='report_detail'),
    path('reports/edit/<int:pk>/', ShiftReportUpdateView.as_view(), name='report_edit'),
    path('reports/delete/<int:pk>/', ShiftReportDeleteView.as_view(), name='report_delete'),

    # Shift report detail view create
    path('report/detail/create/<int:id>/', create_shift_report_detail, name='report_detail_create'),
    path('reports/detail/delete/<int:pk>/', delete_shift_report_detail, name='delete_report_detail'),

   
   

       
   
    # Leave Request URLs


    path('leaves/', LeaveRequestListView.as_view(), name='leave_list'),
    path('leaves/new/', LeaveRequestCreateView.as_view(), name='leave_create'),
    path('leaves/edit/<int:pk>/', LeaveRequestUpdateView.as_view(), name='leave_edit'),
    path('leaves/delete/<int:pk>/', LeaveRequestDeleteView.as_view(), name='leave_delete'),

    # attendance tracking URLs

    path('', attendance_list, name='attendance_list'),
    path('create/', attendance_create, name='attendance_add'),
    path('<int:pk>/edit/', attendance_update, name='attendance_update'),
    path('<int:pk>/delete/', attendance_delete, name='attendance_delete'),
    
    path('report/', attendance_report, name='attendance_report'),


]

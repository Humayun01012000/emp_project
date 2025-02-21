from django.db import models
from datetime import timedelta
from employees.models import Employee 
from datetime import datetime


# Create your models here.

class Shift(models.Model):
    SHIFT_CHOICES =[
        ("A", "Shift A (06:00 AM - 02:00 PM)"),
        ("B", "Shift B (02:00 PM - 10:00 PM)"),
        ("C", "Shift C (10:00 PM - 06:00 AM)"),
    ]

    name = models.CharField(max_length=1, choices=SHIFT_CHOICES, unique=True)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return dict(self.SHIFT_CHOICES).get(self.name, 'Unknown Shift')


class ShiftSchedule(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.employee.name} - {self.shift.name} - {self.start_date} - {self.end_date}"



class ShiftReport(models.Model):
    schedule = models.ForeignKey(ShiftSchedule, on_delete=models.CASCADE)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.schedule.employee.name} - {self.schedule.shift.name} - {self.date}"


class ShiftReportDetail(models.Model):
    report = models.ForeignKey(ShiftReport, on_delete=models.CASCADE)
    task = models.CharField(max_length=100)
    start_time = models.TimeField()
    end_time = models.TimeField()
    duration = models.DurationField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    


    
    
        














    def __str__(self):
        return f"{self.report.schedule.employee.name} - {self.report.schedule.shift.name} - {self.report.date} - {self.task}"
#leave request 

class LeaveRequest(models.Model):
   LEAVE_TYPES =[
        ("Sick", "Sick Leave"),
        ("Vacation", "Vacation Leave"),
        ("Emergency", "Emergency Leave"),
        ("Maternity", "Maternity Leave"),
        ("Paternity", "Paternity Leave"),
        ("Family", "Family Leave"),
        ("Other", "Other"),
   ]


   LEAVE_REASON = [
        ("Sick Leave", "Physical Problem"),
        ("Vacation Leave", "Family Holiday"),
        ("Emergency Leave", "Medical Emergency"),
        ("Maternity Leave", "Maternity Leave"),
        ("Paternity Leave", "Paternity Leave"),
        ("Family Leave", "Family Leave"),
        ("Other", "Other"),
    ]

    
    
   

   STATUS = [
        ("Pending", "Pending"),
        ("Approved", "Approved"),
        ("Denied", "Denied"),
        ("Cancelled", "Cancelled"),
        ("Completed", "Completed"),
   ] 

   employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
   leave_type = models.CharField(max_length=10, choices=LEAVE_TYPES)
   start_date = models.DateField()
   end_date = models.DateField()
   leave_reason = models.CharField(max_length=100, choices=LEAVE_REASON)
   status = models.CharField(max_length=10, choices=STATUS)
   created_at = models.DateTimeField(auto_now_add=True)

   def get_leave_duration(self):
        return (self.end_date - self.start_date).days + 1

   def __str__(self):
        return f"{self.employee.name} - {self.leave_type} - {self.start_date} - {self.end_date} - {self.leave_reason} - {self.status}"


    #leave approval

class LeaveApproval(models.Model):
    LEAVE_APPROVAL_STATUS = [
        ("Pending", "Pending"),
        ("Approved", "Approved"),
        ("Denied", "Denied"),
    ]
    leave_request = models.ForeignKey(LeaveRequest, on_delete=models.CASCADE)
    approver = models.ForeignKey(Employee, on_delete=models.CASCADE)
    approval_status = models.CharField(max_length=10, choices=LEAVE_APPROVAL_STATUS)
    approval_date = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(null=True)
    
    def __str__(self):
        return f"{self.leave_request.employee.name} - {self.leave_request.leave_type} - {self.leave_request.start_date} - {self.leave_request.end_date} - {self.approver.name} - {self.approval_status}"
    #leave attendance
    class Meta:
        verbose_name_plural = "Leave Attendances"

class LeaveAttendance(models.Model):
    leave_approval = models.ForeignKey(LeaveApproval, on_delete=models.CASCADE)
    date = models.DateField()
    is_present = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.leave_approval.leave_request.employee.name} - {self.leave_approval.leave_request.leave_type} - {self.leave_approval.leave_request.start_date} - {self.leave_approval.leave_request.end_date} - {self.date} - {self.is_present}"
    #leave report
    class Meta:
        verbose_name_plural = "Leave Reports"

class LeaveReport(models.Model):
    leave_attendance = models.ForeignKey(LeaveAttendance, on_delete=models.CASCADE)
    report = models.FileField()

    def __str__(self):
        return f"{self.leave_attendance.leave_approval.leave_request.employee.name} - {self.leave_attendance.leave_approval.leave_request.leave_type} - {self.leave_attendance.leave_approval.leave_request.start_date} - {self.leave_attendance.leave_approval.leave_request.end_date} - {self.leave_attendance.date}"
    #leave notification
    class Meta:
        verbose_name_plural = "Leave Notifications"

class LeaveNotification(models.Model):
    leave_report = models.ForeignKey(LeaveReport, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    notification_date = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.leave_report.leave_attendance.leave_approval.leave_request.employee.name} - {self.leave_report.leave_attendance.leave_approval.leave_request.leave_type} - {self.leave_report.leave_attendance.leave_approval.leave_request.start_date} - {self.leave_report.leave_attendance.leave_approval.leave_request.end_date} - {self.leave_report.leave_attendance.date} - {self.employee.name} - {self.notification_date} - {self.is_read}"
    #leave approval history
    class Meta:
        verbose_name_plural = "Leave Approval Histories"

class LeaveApprovalHistory(models.Model):

    LEAVE_APPROVAL_STATUS = [
    ('Pending', 'Pending'),
    ('Approved', 'Approved'),
    ('Rejected', 'Rejected'),
]


    leave_approval = models.ForeignKey(LeaveApproval, on_delete=models.CASCADE)
    previous_status = models.CharField(max_length=10, choices=LEAVE_APPROVAL_STATUS)
    new_status = models.CharField(max_length=10, choices=LEAVE_APPROVAL_STATUS)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.leave_approval.leave_request.employee.name} - {self.leave_approval.leave_request.leave_type} - {self.leave_approval.leave_request.start_date} - {self.leave_approval.leave_request.end_date} - {self.leave_approval.approver.name} - {self.previous_status} - {self.new_status} - {self.updated_at}"
    #leave attendance history
    class Meta:
        verbose_name_plural = "Leave Attendance Histories"


class LeaveAttendanceHistory(models.Model):
    leave_attendance = models.ForeignKey(LeaveAttendance, on_delete=models.CASCADE)
    previous_status = models.BooleanField(default=False)
    new_status = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.leave_attendance.leave_approval.leave_request.employee.name} - {self.leave_attendance.leave_approval.leave_request.leave_type} - {self.leave_attendance.leave_approval.leave_request.start_date} - {self.leave_attendance.leave_approval.leave_request.end_date} - {self.leave_attendance.date} - {self.previous_status} - {self.new_status} - {self.updated_at}"
    #leave report history
    class Meta:
        verbose_name_plural = "Leave Report Histories"


# Complated 

class ComplatedLeave(models.Model):
    leave_request = models.ForeignKey(LeaveRequest, on_delete=models.CASCADE)
    complated_date = models.DateTimeField(auto_now_add=True)
    completed_by = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.leave_request.employee.name} - {self.leave_request.leave_type} - {self.leave_request.start_date} - {self.leave_request.end_date} - {self.completed_by.name} - {self.complated_date}"
    # complated leave history
    class Meta:
        verbose_name_plural = "Completed Leaves"
        


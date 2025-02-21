from django.db import models
from django.db.models import F, ExpressionWrapper, DurationField
from django.core.exceptions import ValidationError

from datetime import timedelta
from employees.models import Employee 
from datetime import datetime, date

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


# employees attendance tracking below  


class Attendance(models.Model):
    STATUS_CHOICES = [
        ('Present', 'Present'),
        ('Absent', 'Absent'),
        ('Late', 'Late'),
        ('Leave', 'Leave'),
    ]

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="attendance_records")
    date = models.DateField(default=date.today)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Absent')
    check_in = models.TimeField(null=True, blank=True)
    check_out = models.TimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        assigned_schedule = ShiftSchedule.objects.filter(
            employee=self.employee, start_date__lte=self.date, end_date__gte=self.date
        ).first()

        if assigned_schedule:
            shift = assigned_schedule.shift
            shift_start = datetime.combine(date.min, shift.start_time)
            shift_end = datetime.combine(date.min, shift.end_time)

            if self.check_in:
                check_in_time = datetime.combine(date.min, self.check_in)
                if check_in_time < shift_start:
                    raise ValidationError("Check-in before shift start is not allowed.")
                elif check_in_time > shift_start + timedelta(minutes=15):  # Allow 15 min buffer
                    self.status = "Late"

            if self.check_out:
                check_out_time = datetime.combine(date.min, self.check_out)
                if check_out_time > shift_end + timedelta(minutes=30):  # Allow 30 min buffer
                    raise ValidationError("Check-out after allowed overtime is not allowed.")

        super().save(*args, **kwargs)

    





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
    

    




    






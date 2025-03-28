# Generated by Django 5.1.6 on 2025-02-20 06:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employees', '0002_alter_employee_employee_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('A', 'Shift A (06:00 AM - 02:00 PM)'), ('B', 'Shift B (02:00 PM - 10:00 PM)'), ('C', 'Shift C (10:00 PM - 06:00 AM)')], max_length=1, unique=True)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='ShiftReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='LeaveApproval',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approval_status', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Denied', 'Denied')], max_length=10)),
                ('approval_date', models.DateTimeField(auto_now_add=True)),
                ('comment', models.TextField(null=True)),
                ('approver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.employee')),
            ],
            options={
                'verbose_name_plural': 'Leave Attendances',
            },
        ),
        migrations.CreateModel(
            name='LeaveApprovalHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('previous_status', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], max_length=10)),
                ('new_status', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], max_length=10)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('leave_approval', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendance.leaveapproval')),
            ],
            options={
                'verbose_name_plural': 'Leave Attendance Histories',
            },
        ),
        migrations.CreateModel(
            name='LeaveAttendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('is_present', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('leave_approval', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendance.leaveapproval')),
            ],
            options={
                'verbose_name_plural': 'Leave Reports',
            },
        ),
        migrations.CreateModel(
            name='LeaveAttendanceHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('previous_status', models.BooleanField(default=False)),
                ('new_status', models.BooleanField(default=False)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('leave_attendance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendance.leaveattendance')),
            ],
            options={
                'verbose_name_plural': 'Leave Report Histories',
            },
        ),
        migrations.CreateModel(
            name='LeaveReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report', models.FileField(upload_to='')),
                ('leave_attendance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendance.leaveattendance')),
            ],
            options={
                'verbose_name_plural': 'Leave Notifications',
            },
        ),
        migrations.CreateModel(
            name='LeaveNotification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification_date', models.DateTimeField(auto_now_add=True)),
                ('is_read', models.BooleanField(default=False)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.employee')),
                ('leave_report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendance.leavereport')),
            ],
            options={
                'verbose_name_plural': 'Leave Approval Histories',
            },
        ),
        migrations.CreateModel(
            name='LeaveRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leave_type', models.CharField(choices=[('Sick', 'Sick Leave'), ('Vacation', 'Vacation Leave'), ('Emergency', 'Emergency Leave'), ('Maternity', 'Maternity Leave'), ('Paternity', 'Paternity Leave'), ('Family', 'Family Leave'), ('Other', 'Other')], max_length=10)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('leave_reason', models.CharField(choices=[('Sick Leave', 'Physical Problem'), ('Vacation Leave', 'Family Holiday'), ('Emergency Leave', 'Medical Emergency'), ('Maternity Leave', 'Maternity Leave'), ('Paternity Leave', 'Paternity Leave'), ('Family Leave', 'Family Leave'), ('Other', 'Other')], max_length=100)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Denied', 'Denied'), ('Cancelled', 'Cancelled'), ('Completed', 'Completed')], max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.employee')),
            ],
        ),
        migrations.AddField(
            model_name='leaveapproval',
            name='leave_request',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendance.leaverequest'),
        ),
        migrations.CreateModel(
            name='ComplatedLeave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complated_date', models.DateTimeField(auto_now_add=True)),
                ('completed_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.employee')),
                ('leave_request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendance.leaverequest')),
            ],
            options={
                'verbose_name_plural': 'Completed Leaves',
            },
        ),
        migrations.CreateModel(
            name='ShiftReportDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=100)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('duration', models.DurationField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendance.shiftreport')),
            ],
        ),
        migrations.CreateModel(
            name='ShiftSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.employee')),
                ('shift', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendance.shift')),
            ],
        ),
        migrations.AddField(
            model_name='shiftreport',
            name='schedule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendance.shiftschedule'),
        ),
    ]

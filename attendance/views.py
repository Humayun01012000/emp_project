from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Shift, ShiftSchedule, ShiftReport, ShiftReportDetail, LeaveRequest
from .forms import ShiftForm, ShiftScheduleForm, ShiftReportForm, ShiftReportDetailForm, LeaveRequestForm
from datetime import datetime 
# Shift Views
class ShiftListView(ListView):
    model = Shift
    template_name = 'attendance/shift/shift_list.html'
    context_object_name = 'shifts'

class ShiftCreateView(CreateView):
    model = Shift
    form_class = ShiftForm
    template_name = 'attendance/shift/shift_form.html'
    success_url = reverse_lazy('shift_list')

class ShiftUpdateView(UpdateView):
    model = Shift
    form_class = ShiftForm
    template_name = 'attendance/shift/shift_form.html'
    success_url = reverse_lazy('shift_list')

class ShiftDeleteView(DeleteView):
    model = Shift
    template_name = 'attendance/shift/shift_confirm_delete.html'
    success_url = reverse_lazy('shift_list')

# Shift Schedule Views
class ShiftScheduleListView(ListView):
    model = ShiftSchedule
    template_name = 'attendance/shift_schedule/schedule_list.html'
    context_object_name = 'schedules'

class ShiftScheduleCreateView(CreateView):
    model = ShiftSchedule
    form_class = ShiftScheduleForm
    template_name = 'attendance/shift_schedule/schedule_create.html'
    success_url = reverse_lazy('schedule_list')


# ShiftScheduleDetailCreateView 

def create_shift_report_detail(request, id):
    report = get_object_or_404(ShiftReport, pk=id)
    
    if request.method == "POST":
        form = ShiftReportDetailForm(request.POST)
        if form.is_valid():
            detail = form.save(commit=False)
            detail.report = report
            
            # Calculate duration automatically
            detail.duration = datetime.combine(datetime.min, detail.end_time) - datetime.combine(datetime.min, detail.start_time)
            
            detail.save()
            messages.success(request, "Shift report detail added successfully!")
            return redirect("report_detail", report.id)  # ✅ Correct way to redirect
    else:
        form = ShiftReportDetailForm()

    return render(request, "attendance/shift_report/report_detail_create.html", {"form": form, "report": report})

def delete_shift_report_detail(request, pk):
    report_detail = get_object_or_404(ShiftReportDetail, pk=pk)
    report_id = report_detail.report.id  # Store the report ID before deleting

    report_detail.delete()
    messages.success(request, "Shift report detail deleted successfully!")
    
    return redirect("report_detail", report_id)  # Redirect back to the report detail page

class ShiftScheduleDetailView(DetailView):
    model = ShiftSchedule
    template_name = 'attendance/shift_schedule/schedule_detail.html'
    context_object_name ='schedule'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['schedule_details'] = ShiftReportDetail.objects.filter(schedule=self.object)
        return context 




class ShiftScheduleUpdateView(UpdateView):
    model = ShiftSchedule
    form_class = ShiftScheduleForm
    template_name = 'attendance/shift_schedule/schedule_form.html'
    success_url = reverse_lazy('schedule_list')

class ShiftScheduleDeleteView(DeleteView):
    model = ShiftSchedule
    template_name = 'attendance/shift_schedule/schedule_confirm_delete.html'
    success_url = reverse_lazy('schedule_list')

# Shift Report Views 



class ShiftReportListView(ListView):
    model = ShiftReport
    template_name = 'attendance/shift_report/report_list.html'
    context_object_name = 'reports'

class ShiftReportCreateView(CreateView):
    model = ShiftReport
    form_class = ShiftReportForm
    template_name = 'attendance/shift_report/report_create.html'
    success_url = reverse_lazy('report_list')

class ShiftReportDetailView(DetailView):
    model = ShiftReport
    template_name = 'attendance/shift_report/report_detail.html'
    context_object_name ='report'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['report_details'] = ShiftReportDetail.objects.filter(report=self.object)
        return context

class ShiftReportUpdateView(UpdateView):
    model = ShiftReport
    form_class = ShiftReportForm
    template_name = 'attendance/shift_report/report_form.html'
    success_url = reverse_lazy('report_list')

class ShiftReportDeleteView(DeleteView):
    model = ShiftReport
    template_name = 'attendance/shift_report/report_confirm_delete.html'
    success_url = reverse_lazy('report_list')

# Leave Request Views


class LeaveRequestListView(ListView):
    model = LeaveRequest
    template_name = 'attendance/leave_report/leave_list.html'
    context_object_name = 'leave_requests'

class LeaveRequestCreateView(CreateView):
    model = LeaveRequest
    form_class = LeaveRequestForm
    template_name = 'attendance/leave_report/leave_create.html'
    success_url = reverse_lazy('leave_list')

class LeaveRequestUpdateView(UpdateView):
    model = LeaveRequest
    form_class = LeaveRequestForm
    template_name = 'attendance/leave_report/leave_form.html'
    success_url = reverse_lazy('leave_list')

class LeaveRequestDeleteView(DeleteView):
    model = LeaveRequest
    template_name = 'attendance/leave_report/leave_confirm_delete.html'
    success_url = reverse_lazy('leave_list')

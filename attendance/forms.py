from django import forms
from .models import Shift, ShiftSchedule, ShiftReport, ShiftReportDetail, LeaveRequest, Attendance
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class ShiftForm(forms.ModelForm):
    class Meta:
        model = Shift
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save Shift'))

class ShiftScheduleForm(forms.ModelForm):
    class Meta:
        model = ShiftSchedule
        fields = ['employee', 'shift', 'start_date', 'end_date']
        widgets = {
            'start_date': forms.DateInput(attrs={
                'type': 'date',  
                'class': 'form-control',  
                'placeholder': 'YYYY-MM-DD'  # Placeholder added
            }),
            'end_date': forms.DateInput(attrs={
                'type': 'date',  
                'class': 'form-control',  
                'placeholder': 'YYYY-MM-DD'  # Placeholder added
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save Schedule'))

class ShiftReportForm(forms.ModelForm):
    class Meta:
        model = ShiftReport
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={
                'type': 'date',  
                'class': 'form-control',  
                'placeholder': 'YYYY-MM-DD'}
            )}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save Report'))

class ShiftReportDetailForm(forms.ModelForm):
    class Meta:
        model = ShiftReportDetail
        fields = ['task', 'start_time', 'end_time']
        widgets = {
            'task': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter task description'}),
            'start_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'end_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save Report Detail'))

class LeaveRequestForm(forms.ModelForm):
    class Meta:
        model = LeaveRequest
        fields = '__all__'
        widgets = {
            
            'start_date': forms.DateInput(attrs={
                'type': 'date',  
                'class': 'form-control',  
                'placeholder': 'YYYY-MM-DD'  # Placeholder added
            }),
            'end_date': forms.DateInput(attrs={
                'type': 'date',  
                'class': 'form-control',  
                'placeholder': 'YYYY-MM-DD'  # Placeholder added
            }),
        }
            

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit Leave Request'))


class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['employee', 'date', 'status', 'check_in', 'check_out']
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'placeholder': 'Select Date'}),
            'check_in': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time', 'placeholder': 'Check-in Time'}),
            'check_out': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time', 'placeholder': 'Check-out Time'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'employee': forms.Select(attrs={'class': 'form-control'}),
        }


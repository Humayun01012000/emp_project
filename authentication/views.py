from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .models import Profile
from .forms import RegisterForm

# def register(request):
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             username = form.cleaned_data.get('username')
#             group = Group.objects.get(name='Student')
#             user.groups.add(group)
#             Proflie.objects.create(user=user)
#             messages.success(request, f'Account created for {username}!')
#             return redirect('login')
#         else:
#             messages.error(request, 'Invalid form!')
#     else:
#         form = RegisterForm()
#     return render(request, 'authentication/register.html', {'form': form})        


@login_required
def dashboard(request):
    return render(request, 'authentication/dashboard.html')
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            employee = Group.objects.get(name='Employee')
            hr = Group.objects.get(name='HR')
            user.groups.add(employee, hr)
            Profile.objects.create(user=user)
            messages.success(request, f'Account created for {user.username}!')
            return redirect('login')
        else:
            messages.error(request, 'Invalid form!')
    else:
        form = UserCreationForm()
    context = {
        'form': form,
    }    
    return render(request,"authentication/register.html",context)           


    


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'authentication/login.html', {'form': form})            

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)  # Pass the request object to logout
        return redirect('login')
    else:
        return redirect('login')  # Redirect to login if the user is not authenticated
    
   
    





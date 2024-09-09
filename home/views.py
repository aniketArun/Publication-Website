from django.shortcuts import render, redirect
from .forms import *
from .models import job_detail, Pricing
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def home_page(request):
    return render(request, 'index.html')

def explore_page(request):
    return render(request, 'explore.html')

def pricing_page(request):
    queryset = Pricing.objects.all()
    return render(request, 'pricing.html', context= {'pricings': queryset})

def about_page(request):
    return render(request, 'about.html')

def career_page(request):
    queryset = job_detail.objects.all()
    return render(request, 'careers.html', context= {'jobs':queryset})

@login_required(login_url='login')
def form_page(request):
    if request.method == 'POST':
        # Create form instance with POST data
        form = IsbnForm(request.POST)
        
        if form.is_valid():  # Check if form data is valid
            form.save()  # This saves the form data to the model
            return redirect('/')  # Redirect to a success page or somewhere else

    else:
        form = IsbnForm()  # Instantiate an empty form for GET requests

    return render(request, 'form.html', {'form': form})

@login_required(login_url='login')
def cover_form_page(request):
    if request.method == 'POST':
        # Create form instance with POST data
        form = CoverdForm(request.POST)
        
        if form.is_valid():  # Check if form data is valid
            form.save()  # This saves the form data to the model
            messages.success(request, "Data Submitted Successfully")
            return redirect('buyisbn')  # Redirect to a success page or somewhere else

    else:
        form = CoverdForm()  # Instantiate an empty form for GET requests
    return render(request, 'form.html', {'form': form})

@login_required(login_url='login')
def edit_form_page(request):
    if request.method == 'POST':
        # Create form instance with POST data
        form = EditBForm(request.POST)
        
        if form.is_valid():  # Check if form data is valid
            form.save()  # This saves the form data to the model
            messages.success(request, "Data Submitted Successfully")
            return redirect('buyedit')  # Redirect to a success page or somewhere else

    else:
        form = EditBForm()  # Instantiate an empty form for GET requests
    return render(request, 'form.html', {'form': form})

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username = username).exists():
            messages.error(request, "Invalid Username")
            return redirect('login')
        
        user = authenticate(request, username = username, password = password)
        if user is None:
            messages.error(request, "Invalid password")
            return redirect('login')
        else:
            login(request, user=user)
            return redirect('/')
            
    return render(request, 'login.html')

def register_page(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username = username).exists():
            messages.error(request, "Username Already Taken")
        else:
            user = User.objects.create(first_name = first_name, last_name = last_name, username = username)

            user.set_password(password)

            user.save()
            messages.success(request, "Account Created Successfully")
            return redirect('login')

            
    return render(request, 'register.html')

def logout_page(request):
    logout(request)
    return redirect('/')
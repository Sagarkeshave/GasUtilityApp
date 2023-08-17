from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ServiceRequestForm , UserRegisterForm, UserCreationForm
from .models import ServiceRequest
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test

# Create your views here.

@login_required
def submit_request(request):
    if request.method == "POST":
        form = ServiceRequestForm(request.POST)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = request.user
            service_request.save()
            return redirect("track_request")

    else:
        form = ServiceRequestForm()
    return render(request, "submit_request.html", {"form":form})

@login_required
def track_request(request):
    requests = ServiceRequest.objects.filter(customer = request.user)
    return render(request, "track_request.html", {"requests" : requests})

@login_required
def manage_request(request):
    if not request.user.is_staff:
        return redirect("track_request")
    requests = ServiceRequest.objects.all()
    return render(request, "manage_request.html", {"requests" : requests})

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def index(request):
    return render(request, "base.html")

def support(request):
    return render(request, "support.html")

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


@login_required
def view_account(request):
    user = request.user
    return render(request, 'view_account.html', {'user': user})

@login_required
@user_passes_test(lambda user: user.is_staff)
def support_tool(request):
    requests = ServiceRequest.objects.all()
    return render(request, 'support_tool.html', {'requests': requests})


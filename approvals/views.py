from django.shortcuts import redirect, render
from .forms import ApplicationForm, CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .authenticate import EmailBackend
from .models import *


# Create your views here.

def loginPage(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        backend = EmailBackend()
        user = EmailBackend.authenticate(backend, request=request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, '!! Username OR password is incorrect !!')

    return render(request, 'approvals/loginPage.html')

def registerPage(request):

    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')

            user = User.objects.get(email=email)
            user.username = email
            user.save()

            messages.success(request, 'Account was created for ' + email)
            return redirect('login')
    
    context = {
        "form":form,
    }
        
    return render(request, 'approvals/registerPage.html', context)

def logoutPage(request):
    logout(request)
    return redirect('login')


def home(request):
    return render(request, 'approvals/homepage.html')

def approvalPage(request):

    user_requests = Request.objects.all()
    users = CustomUser.objects.all()
    context = {
        'user_requests': user_requests,
        'users': users,
    }
    return render(request, 'approvals/approvals.html', context)

def statsPage(request):
    return render(request, 'approvals/stats.html')

def applyPage(request):

    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")

    form = ApplicationForm()
    context = {
        'form': form,
    }
    return render(request, "approvals/apply.html", context)

def viewPage(request, pk):
    application = Request.objects.get(id=pk)
    context = {
        'application':application,
    }
    return render(request, 'approvals/approvalView.html', context)
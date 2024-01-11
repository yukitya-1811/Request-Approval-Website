from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'approvals/homepage.html')

def approvalPage(request):
    return render(request, 'approvals/approvals.html')

def statsPage(request):
    return render(request, 'approvals/stats.html')
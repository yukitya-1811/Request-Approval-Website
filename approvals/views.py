from django.shortcuts import redirect, render
from .forms import ApplicationForm

# Create your views here.

def home(request):
    return render(request, 'approvals/homepage.html')

def approvalPage(request):
    return render(request, 'approvals/approvals.html')

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
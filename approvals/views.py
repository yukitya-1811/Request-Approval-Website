from django.shortcuts import redirect, render
from .forms import ApplicationForm, CreateUserForm, TemplateForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .authenticate import EmailBackend
from .models import *
from .decorators import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

# Create your views here.

@unauthenticated_user
def loginPage(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        backend = EmailBackend()    # Custom class which contains custom authentication functionality

        # Django uses username by default for authentication, but I decided to use
        # email which is what we use for college applications

        user = EmailBackend.authenticate(backend, request=request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, '!! Username OR password is incorrect !!')

    return render(request, 'approvals/loginPage.html')

@unauthenticated_user
def registerPage(request):

    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')

            # initializes a user model with blank username

            user = User.objects.get(email=email)
            user.username = email # sets the username to be equal to email
            user.save()

            messages.success(request, 'Account was created for ' + email)
            return redirect('login')

    
    context = {
        "form":form,
    }
        
    return render(request, 'approvals/registerPage.html', context)

@login_required
def logoutPage(request):
    logout(request)
    return redirect('login')

@login_required
def home(request):
    emps = User.objects.filter(groups__name="employees")
    adms = User.objects.filter(groups__name="admin")

    context = {
        "adms":adms,
        "emps": emps,
    }
    return render(request, 'approvals/homepage.html', context)

@login_required
def approvalPage(request):
    currentuser = request.user.id
    try:
        position = Role.objects.get(user=currentuser) # Only employees are allowed to view the requests of all students
        if position is not None:
            user_requests = Request.objects.all()
            users = CustomUser.objects.all()
            context = {
            'user_requests': user_requests,
            'users': users,
            }
        else: # Students may only view their own requests
            user_requests = Request.objects.all()
            context = {
            'user_requests': user_requests,
            }

    except:
        user_requests = Request.objects.filter(applicant=request.user)
        context = {
            'user_requests': user_requests,
            }

    return render(request, 'approvals/approvals.html', context)

@login_required
@allowed_users(allowed_roles=['employees', 'admin'])
def statsPage(request):
    users = User.objects.all().count()
    reqs = Request.objects.all().count()
    emps = User.objects.filter(groups__name="employees").count()
    studs = User.objects.filter(groups__name="students").count()
    temps = Template.objects.all().count()

    context = {
        'users':users,
        'reqs':reqs,
        'studs':studs,
        'emps':emps,
        'temps':temps,
    }

    return render(request, 'approvals/stats.html', context)

@login_required
def applyPage(request):

    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()

            content = request.POST.get('response')
            req = Request.objects.get(response = content) # Fetches the requests via the content in them. Not the best way to tackling this I admit
            req.applicant = request.user
            req.save() # Sets the applicant of the form as the signed in user
            return redirect("/")

    form = ApplicationForm()
    context = {
        'form': form,
    }
    return render(request, "approvals/apply.html", context)

@login_required
@allowed_users(allowed_roles=['employees', 'admin'])
def viewPage(request, pk):
    application = Request.objects.get(id=pk)
    user = request.user.id
    position = Role.objects.get(user=user)
    participants = application.template_id.participants
    
    context = {
        'participants':participants,
        'application':application,
        'position':position,
    }
    #print(participants) # --> Debugging
    #print(position.name)
    return render(request, 'approvals/approvalView.html', context)

@login_required
@allowed_users(allowed_roles=['employees', 'admin'])
def deleteRequest(request, pk):
    req = Request.objects.get(id=pk)
    if request.method == "POST":
        req.delete()
        return redirect("approvals")
    
    context = { 'request':req, }
    return render(request, 'approvals/deletePage.html', context)

@login_required
@allowed_users(allowed_roles=['employees', 'admin'])
def approveRequest(request, pk):

    req = Request.objects.get(id=pk)
    if request.method == "POST":
        flag = checkUserPerms(request, pk) # Function to verify whether the logged in user should be able to approve the requests
        if flag == 0:
            req.status = "Approved by MIS Officer"
            req.save()
            messages.success(request, "Request approved")
            return redirect('approvals')
        elif flag == 1:
            req.status = "Approved by Head of Department"
            req.save()
            messages.success(request, "Request approved")
            return redirect('approvals')
        elif flag == 2:
            req.status = "Approved by Dean"
            req.save()
            messages.success(request, "Request approved")
            return redirect('approvals')
        else:
            messages.error(request, "You are not authorised to approve the request")
            return redirect('approvals')
        

    context = {'request':req,}
    return render(request, 'approvals/approvePage.html', context)

def checkUserPerms(request, pk):
    user = request.user.id
    req = Request.objects.get(id=pk)
    position = Role.objects.get(user=user)

    if req.status == "Waiting for approval" and position.name == '1':
        return 0
    elif req.status == "Approved by MIS Officer" and position.name == '2':
        return 1
    elif req.status == "Approved by Head of Department" and position.name == '3':
        return 2
    else:
        return
    
    # Not the best way to handle such functionality, as everytime a new position is added
    # will have to write out a lot of code to implement it. But it works for now, assuming
    # that positions are not frequently changed/added

@allowed_users(allowed_roles=['employees', 'admin'])
def createTemplate(request):
    if request.method == "POST":
        form = TemplateForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('home')
    
    form = TemplateForm()

    context = {

        "form": form,
    }
    return render(request, "approvals/createPage.html", context)
    

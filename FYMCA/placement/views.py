from django.shortcuts import render
from .forms import RegisterForms,studendDataForm,companyDetailsForm
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout as logout_auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import signup,studentData,company_details,appliedStudents
from django.contrib.auth.decorators import user_passes_test
# Create your views here.

#
def home(request):
    return render(request,'home.html')

def signup(request):
    form = RegisterForms()
    if request.method == 'POST':
        form = RegisterForms(request.POST)

        if form.is_valid():

            user = form.save()
            user.refresh_from_db()
            raw_password = form.cleaned_data.get('password')
            user.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return HttpResponse("Data saved Succesfully")
    else:
        messages.error(request,"Invalid data")

    return render(request,'signup.html',{'form1':form})

login_required
def studentDataView(request):
    print(request.user)
    form = studendDataForm()
    if request.method=='POST':
        form =studendDataForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            email = request.user

            data.user = email
            data.save()
            return HttpResponse("Student data saved")
        else:
            return HttpResponse("Invalid Data")
    return  render(request,'studentForm.html',{'form':form})

@login_required
def studentSection(request):
    return render(request,'studentSection.html')


@login_required
def profile(request):
    data = studentData.objects.get(user_id=request.user)
    #print(request.user)
    #print(data.skills)
    return render(request,"profile.html",{"data":data})


#Company Details
def check_admin(request):
   return request.is_superuser
@login_required(login_url="/signin")
def notadmin(request):
    return HttpResponse("<h1>You're not an Admin</h1>")
@user_passes_test(check_admin,login_url="/notadmin")
def coordinatorSection(request):
    return render(request,'coordinatorSection.html')

@user_passes_test(check_admin,login_url="/notadmin")
def company_del(request):
    form = companyDetailsForm()
    if request.method=='POST':
        form = companyDetailsForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            return HttpResponse("Student data saved")
        else:
            return HttpResponse("Invalid Data")
    return render(request,'companydetails.html',{'form':form})
@login_required
def user_log(request):
    return HttpResponse("Hey You're Logged in " , request.user.email)

def signin(request):
    if request.user.is_authenticated:
        return render(request,'logout.html')
    else:
        form = AuthenticationForm()
        if request.method == "POST":
            email = request.POST['username']
            password =request.POST['password']
            user =authenticate(request,email=email,password=password)
            print("USer: " , user)
            if user is not None:
                login(request,user)

            else:
                messages.error(request,"Invalid Credentials")
                return HttpResponse("Invalid Credentials")


    return render(request,'signin.html',{'form':form})

def logout(request):
    if request.user.is_authenticated:
        logout_auth(request)
        messages.success(request,'You logged out')
        return redirect('/signin')
    else:
        return HttpResponse("You're not logged in")
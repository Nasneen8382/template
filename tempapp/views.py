from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth

from tempapp.models import Theme

# Create your views here.

def loginpage(request):
    return render(request,'login.html')
def logout(request):
	auth.logout(request)
	return redirect('loginpage')

def login(request):
    if request.method== 'POST':
        usrname=request.POST['uname']
        pswd=request.POST['pwd']
        user = auth.authenticate(username=usrname, password=pswd)
        # teacher= TeacherModel.objects.get(id=user.id)
        if user is not None:
            if user.is_staff:
                auth.login(request, user)
                return redirect('admin')
            else:
                auth.login(request, user)
                return redirect('index')
        else:
            return redirect('loginpage')
    else:
         return redirect('loginpage')


def admin(request):
    thm = Theme.objects.get(status='active')
    return render(request,'admin.html',{'theme':thm})
def index(request):
    thm = Theme.objects.get(status='active')
    return render(request,'index2.html',{'theme':thm})

def signuppage(request):
    return render(request,'signup.html')


def signup(request):
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        uname=request.POST['uname']
        password = request.POST['pwd']

        if User.objects.filter(username=uname).exists():
            return redirect('signuppage')
        elif User.objects.filter(email=email).exists():
            return redirect('signuppage')
        else:
            user= User.objects.create_user(first_name=fname,last_name=lname,username=uname,email=email,password=password)
            user.save()
            data=User.objects.get(id=user.id)
            return redirect('loginpage')
    else:
         return redirect('loginpage')
    
def themechange(request,nam):
    print(nam)
    thm = Theme.objects.filter(status='active')
    for i in thm:
        i.status='inactive'
        i.save()
    
    th = Theme.objects.get(name=nam)
    th.status='active'
    th.save()

    return redirect('admin')
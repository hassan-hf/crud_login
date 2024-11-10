from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as lin,logout as logo
from django.contrib.auth.decorators import login_required
from .forms import User_form
from .models import Users


def register(request):
    if request.method=='POST':
        name=request.POST.get('uname')
        email=request.POST.get('email')
        password=request.POST.get('pass1')
        password2=request.POST.get('pass2')
        if password != password2:
            return HttpResponse('password1 and password2 are not equal')

        else:
            saver =User.objects.create_user(username=name ,password=password)
            saver.save()
        return redirect('login')
    return render(request,'register.html')




def login(request):
    if request.method=='POST':
        name=request.POST.get('uname')
        password =request.POST.get('password')
        usse=authenticate(request,username=name,password=password)
        print(usse)
        if usse is not None:
            lin(request,usse)
            return redirect('add')
        else:
            return redirect('register')

    return redirect(request,'login.html')


@login_required
def home(request):
        return render(request,'home.html')

def send(request):
    return render(request,'logout.html')

def logout(request):
    logo(request)
    return redirect('send')


def add(request):
    if request.method=='POST':
        fm=User_form(request.POST)
        if fm.is_valid():
            fm.save()
            fm=User_form()
        else:
            fm=User_form()
            sm = Users.objects.all()
            return render(request,'add.html',{'form':fm,'stu':sm})



def delete(request):
    if request.method=='POST':
        d1=Users.objects.get(pk=id)
        d1.delete()

    else:
        d1=User_form(request.POST)
        return redirect('add')


def update(request,id):


    if request.method=='POST':

        sm = Users.objects.get(pk=id)
        fm = User_form(request.POST,instance=sm)
        if fm.is_valid():
            fm.save()
            fm = User_form()
    else:
        sm = Users.objects.get(pk=id)
        fm = User_form(instance=sm)
    return render(request,'update.html',{'form':fm})
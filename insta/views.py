import email
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    return render(request,'index.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        email = request.POST['email']

        myuser = User.objects.create_user(username,email,pass1)
        myuser.save()
        messages.success(request,'You have successfully signed up!')

        redirect('login')
    return render(request,'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        user = authenticate(username=username,password=pass1)
        if user is not None:
            login(request,user)
            messages.success(request,'You have successfully logged in!')
            return redirect('index')
        else:
            messages.error(request,'Invalid credentials!')
        return redirect('index')


    return render(request,'login.html')

def logout(request):
    pass
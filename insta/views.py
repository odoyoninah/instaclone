import email
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages

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

        return redirect('login')





    return render(request,'signup.html')

def login(request):
    return render(request,'login.html')

def logout(request):
    pass
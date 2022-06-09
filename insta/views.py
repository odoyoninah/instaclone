import email
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import User,Image,Comment,Like,Follow
from .forms import ImageForm, RegisterForm
from django.contrib.auth.decorators import login_required


def index(request):
    images=Image.objects.all()
    return render(request,'index.html',{'images':images})

def comment(request,id):
    image=Image.objects.get(id=id)
    if request.method=='POST':
        comment=request.POST['comment']
        user=User.objects.get(id=request.user.id)
        new_comment=Comment(comment=comment,user=user,image=image)
        new_comment.save()
        return redirect('index')

def like(request,id):
    image=Image.objects.get(id=id)
    user=User.objects.get(id=request.user.id)
    new_like=Like(user=user,image=image)
    new_like.save()
    return redirect('index')

def follow(request,id):
    user=User.objects.get(id=id)
    follower=User.objects.get(id=request.user.id)
    new_follow=Follow(user=user,follower=follower)
    new_follow.save()
    return redirect('index')



@login_required(login_url='/accounts/login/')
def createpost(request):
    if request.method=='POST':
        form = ImageForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()

            return redirect('index')
    else:
        form = ImageForm()
    return render(request,'createpost.html',{'form':form}) 


def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()


   

        return redirect('login')
    else:    
        form = RegisterForm()
    return render(request,'registration/signup.html',{'form':form})

    
def logout(request):
    logout(request)
    messages.success(request,'You have successfully logged out!')
    return redirect('index')

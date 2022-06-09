import email
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import User,Image,Comment,Like,Follow
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt


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

def createpost(request):
    if request.method=='POST':
        image=request.FILES['image']
        caption=request.POST['caption']
        user=User.objects.get(id=request.user.id)
        new_image=Image(image=image,caption=caption,user=user)
        new_image.save()
        messages.success(request,'Your post has been created!')
        return redirect('index')
    else:
        return render(request,'createpost.html')


@csrf_exempt
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

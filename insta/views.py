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

# Create your views here.
# def index(request):
#     return render(request,'index.html')

def index(request):
    images=Image.objects.all()
    return render(request,'index.html',{'images':images})

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

# @login_required
# def instagram(request):
#     return render(request,'index.html')




@csrf_exempt
def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
    #         messages.success(request,'You have successfully registered!')
    #         return redirect('index')
    #     username = request.POST['username']
    #     pass1 = request.POST['pass1']
    #     pass2 = request.POST['pass2']
    #     email = request.POST['email']

    #     myuser = User.objects.create_user(username,email,pass1)
    #     myuser.save()
    #     messages.success(request,'You have successfully signed up!')

        return redirect('login')
    else:    
        form = RegisterForm()
    return render(request,'registration/signup.html',{'form':form})

    

# def login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         pass1 = request.POST['pass1']
#         user = authenticate(username=username,password=pass1)
#         if user is not None:
#             login(request,user)
#             messages.success(request,'You have successfully logged in!')
#             return redirect('index')
#         else:
#             messages.error(request,'Invalid credentials!')
#         return redirect('index')


#     return render(request,'login.html')

def logout(request):
    logout(request)
    messages.success(request,'You have successfully logged out!')
    return redirect('index')

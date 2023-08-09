
from django.shortcuts import render
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .forms import LoginForm
from .forms import UserRegistrationForm
from .models import CustomUser
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    username = request.user.username 
    return render(request, 'index.html', {'username': username})
    # user = request.user 
    # print(user.)
    # return render(request,'index.html',{})
    # return render(request, 'index.html')

# def register(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         cpassword = request.POST.get('password1')
#         if password == cpassword:
#             if User.objects.filter(username=username).exists():
#                 messages.info(request, "username taken")
#                 return redirect('register')
#             elif User.objects.filter(email=email).exists():
#                 messages.info(request, "email taken")
#                 return redirect('register')
#             else:
#                 user = User.objects.create_user('username','email','password')


#                 user.save()
#                 return redirect('login')

#         else:
#           messages.info(request, "password not matching")
#         return redirect('register')




#     return render(request, 'register.html', {})

# def login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = auth.authenticate(username=username, password=password)

#         if user is not None:
#             auth.login(request, user)
#             return redirect('home')
#         else:
#             messages.info(request, "invalid credentials")
#             return redirect('login')


#     return render(request, 'login.html', {})

def form(request):
    return render(request, 'form.html', {})

def logout(request):
    auth.logout(request)
    return redirect('home')









# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#     else:
#         form = UserCreationForm()
#     return render(request, 'register.html', {'form': form})

def register(request):
    if request.method == 'POST':
       
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
          
            print(form.cleaned_data)
            user = form.save()
            print(user)
            form.save()
        
            return redirect('login',)  
        else:
            print(form.errors)  
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})


# def login(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():

#             return redirect('home')  # Replace 'home' with the name of your homepage view or URL pattern
#     else:
#         form = AuthenticationForm()
#     return render(request, 'login.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            print(user)  
            login(request, user)
            # return redirect('home',user) 
            return redirect('form')  # Pass username to 'home' view

        else:
            print(form.errors)  

    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


from django.shortcuts import render
from .models import CustomUser
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
# Create your views here.

def create_user_view(request):#make new view to create user
    name = request.POST.get('name')
    surname = request.POST.get('surname')
    username = request.POST.get('username')
    email = request.POST.get('email')
    pass1 = request.POST.get('pass1')
    pass2 = request.POST.get('pass2')
    gender = request.POST.get('gender')
    dob = request.POST.get('dob')
    if pass1 != pass2:
        return render(request, 'nope.html')
    user = CustomUser.objects.create_user(first_name = name, last_name = surname, username = username, email = email, password = pass1)
    user.save()
    return render(request, 'home.html' )

def register_page_view(request):
    return render(request, 'registration/register.html')

def login_user_view(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    user = authenticate(username = email, password = password)
    print(user)
    if user is not None:
        login(request, user)
        return render(request, 'home.html')
    else:
        return render(request, 'nope.html')

def login_page_view(request):
    return render(request, 'registration/login.html')
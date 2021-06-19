from django.shortcuts import redirect, render
from .models import CustomUser
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from profiles.models import Profile

def create_user_view(request):  # make new view to create user
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
    user = CustomUser.objects.create_user(
        first_name=name, last_name=surname, username=username, email=email, password=pass1)
    user.save()
    user_profile = Profile.objects.create(user = user)
    user_profile.save()    
    
    return render(request, 'home.html')


def register_page_view(request):
    return render(request, 'registration/register.html')


def login_user_view(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    user = authenticate(username=email, password=password)
    context = {
        'check'  : False,
        'message': 'Incorrect username or password.'
    }
    print(user)
    if user is not None:
        login(request, user)
        return render(request, 'home.html')
    else:
        return render(request, 'registration/login.html', context)


def login_page_view(request):
    context = {
        'check'  : True,
        'message': 'Incorrect username or password.'
    }
    return render(request, 'registration/login.html', context)

def search_user_view(request):
    to_search = request.POST.get('search_user')
    found_user = CustomUser.objects.filter(username = to_search)
    print(found_user)
    context = {
        'search_user' : to_search,
        'found_users'  : found_user,
    }
    return render(request, 'search.html', context)
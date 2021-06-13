from django.shortcuts import render
from users.models import CustomUser
from .models import Profile

def profile_page_view(request, username):
    user = CustomUser.objects.get(username=username)
    profile = Profile.objects.get(user=user)
    posts = user.post_set.all()
    context = {
        'profile' : profile,
        'posts'   : posts,
    }
    return render(request, 'profile.html', context)
from django.shortcuts import redirect, render
from users.models import CustomUser
from .models import Profile

def profile_page_view(request, username):
    current_user = request.user
    user = CustomUser.objects.get(username=username)
    profile = Profile.objects.get(user=user)
    if current_user in profile.followers.all():
        check = True
    posts = user.post_set.all()
    context = {
        'profile' : profile,
        'posts'   : posts,
        'check'   : check,
    }
    return render(request, 'profile.html', context)

def follow_user_view(request, user1, user2):
    follower = CustomUser.objects.get(username = user1)
    to_follow = CustomUser.objects.get(username = user2)
    follower_profile = Profile.objects.get(user = follower)
    to_follow_profile = Profile.objects.get(user = to_follow)
    if follower not in to_follow_profile.followers.all():
        follower_profile.following.add(to_follow)
        to_follow_profile.followers.add(follower)
        follower_profile.following_count += 1
        to_follow_profile.followers_count += 1
        follower_profile.save()
        to_follow_profile.save()
        return redirect('profile', user2)
    
    else:
        return redirect('profile', user2)


         




    
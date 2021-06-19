from django.urls import path
from .views import profile_page_view, follow_user_view

urlpatterns = [
    path('<str:username>', profile_page_view, name = 'profile'),
    path('<str:user1>/follow/<str:user2>', follow_user_view, name = 'follow'),
]
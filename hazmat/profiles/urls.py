from django.urls import path
from .views import profile_page_view


urlpatterns = [
    path('<str:username>', profile_page_view, name = 'profile'),
]
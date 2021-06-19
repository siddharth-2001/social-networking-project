from django.urls import path
from .views import create_user_view, register_page_view, login_user_view, login_page_view, search_user_view


urlpatterns = [
    path('register', register_page_view, name = 'register'),
    path('register/submit', create_user_view, name = 'register_submit'),
    path('login/', login_page_view, name = 'login'),
    path('login/submit', login_user_view, name = 'login_submit'),
    path('search', search_user_view, name= 'search' ),
]
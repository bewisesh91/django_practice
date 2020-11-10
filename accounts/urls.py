from django.urls import path
# from 다음에 . 은 urls.py를 포함한 현재 위치(posts)를 의미
from . import views

app_name = 'accounts'
urlpatterns = [
        path('sign-up/', views.sign_up, name = 'sign_up'),
        path('login/', views.login, name = 'login'),
        path('logout/', views.logout, name = 'logout'),
]

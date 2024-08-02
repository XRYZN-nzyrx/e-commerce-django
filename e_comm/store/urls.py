# store/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('log/', views.log, name='log'),
    #path('', views.home, name='home'),  # Assuming you have a home view
    path('signup/',views.signup,name='signup'),
    path('sign/',views.sign,name='sign'),
    path('home/',views.home,name='home')

]

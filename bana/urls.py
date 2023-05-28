from django.contrib import admin
from django.urls import path,include
from bana import views
from django.contrib.auth import views as auth
# from . import views

urlpatterns = [
      path('signup/',views.handlesignup, name='signup'),
      path('home/',views.home, name='home'),
      path('logout/',views.home, name='home'),    
      path('login/',views.handlelogin, name='login'),
      path('signout/',views.handlesignout, name='signout'),
      path('' , views.home,name='home'),
    #   path('',views.handlesignup, name='signup'),
    #   path('',views.handlesignup, name='signup'),
    #   path('',views.handlesignup, name='signup'),
    #   path('',views.handlesignup, name='signup'),
    #   path('',views.handlesignup, name='signup'),

    # path('signup/login/home/',views.home, name='home'),
    # path('free_wifi',views.free_wifi, name='free_wifi'),
    # path('own_a_router/',views.own_a_router, name='own_a_router'),
    # path('subscription_plans/',views.subscription_plans, name='subscription_plans'),
    # path('signup/',views.handlesignup, name='handlesignup'),
    # path('login/',views.handlelogin, name='handlelogin'),
    # path('login/home/login',views.home, name='handlelogin'),
    # path('signup/home/',views.home, name='handlelogin'),
    # path('logout/', auth.LogoutView.as_view(template_name ='index.html'), name ='logout'),


#    path('', views.bana, name=''),

]

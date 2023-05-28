"""
URL configuration for avan project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from bana import views
from django.contrib.auth import views as auth
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

urlpatterns = [
      path('admin/', admin.site.urls),
      path('home/', views.home , name='home'),
      path('', views.home , name='home'),
      path('home/logout/' , views.handlesignout, name='signout'),
      path('home/login/' , views.handlelogin, name='login'),
      path('home/signup/' , views.handlesignup, name='signup'),
      path('free_wifi/', views.free_wifi,name='free_wifi'),
      path('own_a_router/', views.own_a_router,name='own_a_router'),
      path('subscription_plans', views.subscription_plans,name='subscription_plans'),
      path('signup/', include('bana.urls')),
      path('login/',views.handlelogin, name='handlelogin'),
      path('logout/',views.handlesignout, name='handlesignout'),
      path('askinggateway/paytmgateway/',views.paytmgateway, name='purchase'), 
      path('askinggateway/stripegateway/',views.stripegateway, name='stripegateway'), 
      path("handlerequest/", views.handlerequest, name="HandleRequest"),
      path("askinggateway/", views.askinggateway, name="askinggateway"),
   #   path("razorpaypayment/", views.razorpaypayment, name="razorpaypayment"),
      path('paymenthandler/', views.paymenthandler, name='paymenthandler'),
      path('askinggateway/paymenthandler/', views.paymenthandler, name='paymenthandler'),

      
    #   path('create-checkout-session/', views.createcheckoutsessionview,name='checkoutsessionview')
    #  url(r'^paytm/', include('paytm.urls')),
]

# urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
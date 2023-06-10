"""eecom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from eecomapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('Shop/',views.Shop,name='Shop'),
    path('about/',views.about,name='about'),
    path('Signup/',views.Signup,name='Signup'),
    path('Login/',views.Login,name='Login'),
    path('add_to_cart/',views.add_to_cart,name='add_to_cart'),
    path('carts/',views.carts,name='carts'),
    path('Contact/',views.Contact,name='Contact')
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

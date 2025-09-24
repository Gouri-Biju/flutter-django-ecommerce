"""ecommerce_backend URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from .import views
urlpatterns = [
    path('reg/',views.ureg),
    path('login/',views.login_post),
    path('products/<uid>',views.viewproduct),
    path('addtocart/<pid>/<uid>',views.addtocart),
    path('cart/<uid>',views.viewcart),
    path('qupdate/<oid>/<str:q>/',views.updatequantity),
    path('qupdate/<oid>/<str:q>/',views.updatequantity),
    path('buy/<uid>/',views.buy),
    path('history/<uid>/',views.history),
    path('manageproductview/',views.manageproductview),
    path('addproducts/',views.addproducts),
    path('pedit/<str:pid>/',views.pedit),
    path('pdelete/<str:pid>/',views.pdelete),
    path('orders/',views.orders),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
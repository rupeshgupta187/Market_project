from django.urls import path
from . import views
urlpatterns=[
    path('index/', views.index),
    path('', views.index),
    path('about/', views.about),
    path('contact/', views.contact),
    path('signin/', views.signin),
    path('myorder/', views.Myorder),
    path('product/', views.product),
    path('view/', views.viewproduct),
    path('mens/', views.mens),
    path('womens/', views.womens),
    path('kids/', views.kids),

]
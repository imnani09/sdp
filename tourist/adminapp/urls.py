from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('login/', views.loginpage,name='loginpage'),
    path('register/', views.registerpage, name='registerpage'),
    path('about/',views.aboutpage,name='aboutpage'),
    path('contact/',views.contactpage,name='contactpage'),
    path('feedback/',views.feedbackpage,name='feedbackpage'),
    path('registeruser/',views.registeruser,name='registeruser'),
    path('loginuser/',views.loginuser,name='loginuser'),
    path('packages/',views.packagespage,name='packagespage'),
    path('hotels/',views.hotelspage,name='hotelspage'),
    path('travel/',views.travelpage,name='travelpage'),
    path('accomadation/',views.accomadationpage,name='accomadationpage'),
    path('luxury/',views.luxpage,name='luxpage'),
    path('deluxe/',views.delxpage,name='delxpage'),
    path('hotelspaymentpage/',views.hotelspaymentpage,name='hotelspaymentpage'),
    path('standard/',views.stndpage,name='stndpage'),
    path('transportation/',views.transportationpage,name='transportationpage'),
    path('payments/',views.paymentspage,name='paymentspage'),
    path('logout/', views.logout_the_page, name='logoutPage'),
]

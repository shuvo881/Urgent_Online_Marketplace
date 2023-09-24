from django.contrib import admin
from django.urls import path, include
from .views import index, contact, signup, signin, signout
urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('signout/', signout, name='signout'),

]

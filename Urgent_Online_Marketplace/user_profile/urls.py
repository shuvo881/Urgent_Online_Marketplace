from django.urls import path
from .views import user_profile, _profile_edit, user_delete

urlpatterns = [
    path('profile/<str:username>/', user_profile, name='user_profile'),
    path('<str:username>/edit/', _profile_edit, name='_profile_edit'),
    path('user_delete/', user_delete, name='user_delete'),

]
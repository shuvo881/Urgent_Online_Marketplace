from django.urls import path
from .views import details


urlpatterns = [
    path('<int:pk>/', details, name='details'),
]

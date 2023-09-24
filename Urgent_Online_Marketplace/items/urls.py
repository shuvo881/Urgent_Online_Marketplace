from django.urls import path
from .views import details, new_item_add


urlpatterns = [
    path('<int:pk>/', details, name='details'),
    path('new/', new_item_add, name='new_item_add'),

]

from django.urls import path
from .views import details, new_item_add, delete_item, edit_item, browser


urlpatterns = [
    path('<int:pk>/', details, name='details'),
    path('new/', new_item_add, name='new_item_add'),
    path('<int:pk>/delete_item', delete_item, name='delete_item'),
    path('<int:pk>/edit_item', edit_item, name='edit_item'),
    path('', browser, name='browser'),

]

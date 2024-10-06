from django.urls import path
from .views import *
#import obtain_auth_token view
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('menu', MenuItemsView.as_view(), name="api_menu"),
    path('menu/<int:pk>/', SingleMenuItemView.as_view(), name="api_single_menu"),
    path('menu-items', MenuItemsView.as_view(), name="api_menu"),
    path('menu-items/<int:pk>/', SingleMenuItemView.as_view(), name="api_menu_item"),
    path('api-token-auth/', obtain_auth_token),
]

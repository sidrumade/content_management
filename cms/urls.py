from rest_framework.authtoken import views
from django.urls import path,include
from .views import home,get_username


app_name = 'cms'

urlpatterns = [
    path('',home,name='home'),
    path('getuser/',get_username,name='getuser'),
    path('api-token-auth/', views.obtain_auth_token),
]
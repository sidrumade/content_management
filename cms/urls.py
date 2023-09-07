from rest_framework.authtoken import views as rest_view
from django.urls import path,include
from .views import home,get_username,create_author
from .views import ContentViewSet, CategoryViewSet
from .serializers import ContentSerializer, CategorySerializer



app_name = 'cms'

urlpatterns = [
    path('',home,name='home'),
    path('getuser/',get_username,name='getuser'),
    path('api-token-auth/', rest_view.obtain_auth_token),
    path('create_author/', create_author, name='create_author'),
    
    #add content and category viewset
]
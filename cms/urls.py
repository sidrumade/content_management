from rest_framework.authtoken import views as rest_view
from django.urls import path
from .views import home,get_username,create_author
from .views import ContentViewSet, CategoryViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'content', ContentViewSet, basename='content')
router.register(r'category', CategoryViewSet, basename='category')

app_name = 'cms'

urlpatterns = [
    path('',home,name='home'),
    path('getuser/',get_username,name='getuser'),
    path('api-token-auth/', rest_view.obtain_auth_token),
    path('create_author/', create_author, name='create_author'),
    
    #add content and category viewset
]
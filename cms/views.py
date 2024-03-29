from django.http import JsonResponse

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status , viewsets

from .serializers import AuthorSerializer,CategorySerializer,ContentSerializer
from .models import Content,Category
from .permissions import IsAuthorOrAdmin


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_username(request):
    content = {
        'user': str(request.user),
    }
    return Response(content)


def home(request):
    return JsonResponse({'status':'success'})


    
@api_view(['POST'])  # This view only accepts POST requests
def create_author(request):
    if request.method == 'POST':
        # Create an instance of AuthorSerializer with the request data
        serializer = AuthorSerializer(data=request.data)

        # Validate the data
        if serializer.is_valid():
            # Save the validated data to the database
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    


class ContentViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    permission_classes = [IsAuthorOrAdmin]       # Only allow the content owner to change the content


    def perform_update(self, serializer):
        serializer.save(author=self.request.user)
        
    def get_queryset(self):
        if self.request.user.is_superuser:
            return Content.objects.all()  #list all objects
        return Content.objects.filter(author=self.request.user)  # list only perticular authors object
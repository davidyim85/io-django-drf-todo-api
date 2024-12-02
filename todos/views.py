from .models import Todo
from rest_framework import viewsets, permissions, status
from .serializers import TodoSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response

class TodoViewSet(viewsets.ModelViewSet):
    #every in the todo object is able to be seen in the view
    queryset=Todo.objects.all()
    #specifies which serializer to use. in this case, we will be using the file serializer and in that file 
    # the class called TodoSerializer
    serializer_class=TodoSerializer
    # unrestricted access to the api
    permission_classes=[IsAuthenticated]

    # Automatically associate the book with the authenticated user
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    # only return book owned by the authenticated user
    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)


class UserRegistrationView(APIView):
    permission_classes=[AllowAny]
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

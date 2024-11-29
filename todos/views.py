from .models import Todo
from rest_framework import viewsets, permissions
from .serializers import TodoSerializer

class TodoViewSet(viewsets.ModelViewSet):
    #every in the todo object is able to be seen in the view
    queryset=Todo.objects.all()
    #specifies which serializer to use. in this case, we will be using the file serializer and in that file 
    # the class called TodoSerializer
    serializer_class=TodoSerializer
    # unrestricted access to the api
    permission_classes=[permissions.AllowAny]
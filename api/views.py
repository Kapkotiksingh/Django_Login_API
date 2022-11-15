# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .models import *
# from .serializers import *

# # FBV for list of all Todo objects
# @api_view(['GET', 'POST'])

# def todo_list(request):
#     """
#     List all code todos, or create a new todo.
#     """
#     if request.method == 'GET':
#         todos = Todo.objects.all()
#         serializer = TodoSerializer(todos, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = TodoSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'DELETE'])
# def todo_detail(request, pk):
#     """
#     Retrieve, update or delete a code todo.
#     """
#     try:
#         todo = Todo.objects.get(pk=pk)
#     except Exception as e:
#         return Response(str(e),status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = TodoSerializer(todo)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = TodoSerializer(todo, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         todo.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)




from .models import *
from .serializers import *
from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.models import User, Group
from rest_framework import permissions, viewsets




class TodoList(generics.ListAPIView):
    queryset = Todo.objects.all()
    # View-level permissions
    # IsAuthenticatedOrReadOnly, which will ensure that authenticated requests get read-write access,
    # and unauthenticated requests get read-only access.
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = TodoSerializer



class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    # View-level permissions
    # IsAuthenticatedOrReadOnly, which will ensure that authenticated requests get read-write access,
    # and unauthenticated requests get read-only access.
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = TodoSerializer



class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

# from rest_framework.authtoken.models import Token

# token = Token.objects.create(user="c70b234dedb543dbe3270dde122843a509a64829")
# print("@@@@@@@@@",token.key))
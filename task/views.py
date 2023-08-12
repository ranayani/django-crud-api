from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from task.serializers import TodoSerializer
from task.models import Todo

# Create your views here.
#def index(request):
#    return HttpResponse("Hello World")

#def project(request):
#    return HttpResponse("This is project View")

class ListTaskAPIView(ListAPIView):
    """This endpoint list all of the available todos from the database"""
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class CreateTaskAPIView(CreateAPIView):
    """This endpoint allows for creation of a todo"""
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class UpdateTaskAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific todo by passing in the id of the todo to update"""
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class DeleteTaskAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific Todo from the database"""
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

from django.shortcuts import render
# we import Django REST Framework’s generics views and both our models.py and
# serializers.py files.

# Create your views here.
from rest_framework import generics
from .models import Todo
from .serializers import TodoSerializer
# from our todos/urls.py we had two views.
# so in our model We will use ListAPIView37 to
# display all todos and RetrieveAPIView38 to display a single model
# instance
class ListTodo(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class DetailTodo(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
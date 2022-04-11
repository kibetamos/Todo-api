from rest_framework import serializers # we import the serializer fom the rest framework
from .models import Todo #import models from todoapp

#create a serializer classs
class TodoSerializer(serializers.ModelSerializer):
    # We’re specifying which model to use and the specific fields on it we want to expose
    class Meta:
        model = Todo
        fields = ('id', 'title', 'body',)
# Django REST Framework will now magically transform our data into JSON exposing
# the fields for id, title, and body from our Todomodel.
#we serailze so that we get our data in form of JSON format


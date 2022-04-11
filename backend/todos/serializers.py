from rest_framework import serializers # we import the serializer fom the rest framework
from .models import Todo #import models from todoapp

#create a serializer classs
class TodoSerializer(serializers.modelSerializer):
    # We’re specifying which model to use and the specific fields on it we want to expose
    class Meta:
        model=todo
        fields = ('id', 'title', 'body',)
# Django REST Framework will now magically transform our data into JSON exposing
# the fields for id, title, and body from our Todomodel.

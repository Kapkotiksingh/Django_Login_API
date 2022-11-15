from rest_framework import serializers
from django.contrib.auth.models import User, Group
from .models import *

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        # fields = ('id', 'title', 'description', 'completed')
        # Shortcut for getting all fields
        fields = '__all__'

class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = "__all__"

class GroupSerializer(serializers.Serializer):
    class Meta:
        model = Group
        fields = "__all__"        

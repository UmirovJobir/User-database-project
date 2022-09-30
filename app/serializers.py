from dataclasses import field
from email.policy import default
from pyexpat import model
from rest_framework import serializers
from .models import User, Post, Category
from rest_framework.response import Response
from rest_framework import status
from rest_framework.validators import UniqueValidator


class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ["id", "first_name", "last_name", "username", "city"]



class RegisterSerializer(serializers.ModelSerializer):
  class Meta:
      model = User
      fields = ('username', 'password','email', 'first_name', 'last_name', 'city')

  def create(self, validated_data):
      user = User.objects.create(
        username=validated_data['username'],
        password=validated_data['password'],
        email=validated_data['email'],
        # first_name=validated_data['first_name'],
        # last_name=validated_data['last_name'],
        city = validated_data['city']
      )
      user.set_password(validated_data['password'])
      user.save()
      return user


class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = ('name',)


class PostCreateSerializer(serializers.ModelSerializer):
  user = serializers.HiddenField(default=serializers.CurrentUserDefault())
  class Meta:
    model = Post
    fields = ('title', 'content', 'category', 'user')

class PostGetSerializer(serializers.ModelSerializer):
  class Meta:
    model = Post
    fields = ('title', 'content', 'category', 'user')
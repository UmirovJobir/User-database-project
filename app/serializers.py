
from pyexpat import model
from rest_framework import serializers
from .models import User, Document, Additional_document
from rest_framework.response import Response
from rest_framework import status
from rest_framework.validators import UniqueValidator


class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ["id", "first_name", "last_name", "username", "photo"]


class RegisterSerializer(serializers.ModelSerializer):
  class Meta:
      model = User
      fields = ('username', 'password','email', 'first_name', 'last_name',"photo")

  def create(self, validated_data):
      user = User.objects.create(
        username=validated_data['username'],
        password=validated_data['password'],
        email=validated_data['email'],
        first_name=validated_data['first_name'],
        last_name=validated_data['last_name'],
        photo = validated_data["photo"]
      )
      user.set_password(validated_data['password'])
      user.save()
      return user


class DocumentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Document
    fields = ('user',"passport",'CV','military_ID','reference','diplom','driving_license')
    # fields = ('__all__')

class AddDocSerializer(serializers.ModelSerializer):
  class Meta:
    model = Additional_document
    fields = ('user', 'title', 'file')

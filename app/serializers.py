
from pyexpat import model
from urllib import request
from rest_framework import serializers
from rest_framework.serializers import CurrentUserDefault
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
      fields = ('username', 'password','email',"photo")

  def create(self, validated_data):
      user = User.objects.create(
        username=validated_data['username'],
        password=validated_data['password'],
        email=validated_data['email'],
        photo = validated_data["photo"]
      )
      user.set_password(validated_data['password'])
      user.save()
      return user

class DocumentGetSerializer(serializers.ModelSerializer):
  class Meta:
    model = Document
    fields = ('id','user', "passport",'CV','military_ID','reference','diplom','driving_license')

class DocumentPostSerializer(serializers.ModelSerializer):
  user = serializers.HiddenField(default=CurrentUserDefault())
  class Meta:
    model = Document
    fields = ('user', "passport",'CV','military_ID','reference','diplom','driving_license')
  
  # def create(self, validated_data): 
  #       document = Document.objects.create( 
  #         passport=validated_data['passport'],
  #         CV=validated_data['CV'],
  #         military_ID=validated_data['military_ID'],
  #         reference=validated_data['reference'],
  #         diplom=validated_data['diplom'],
  #         driving_license=validated_data['driving_license']
  #       )
  #       document.save()
  #       return document

class AddDocGetSerializer(serializers.ModelSerializer):
  class Meta:
    model = Additional_document
    fields = ('id', 'user', 'title', 'file')

class AddDocPostSerializer(serializers.ModelSerializer):
  user = serializers.HiddenField(default=CurrentUserDefault())
  class Meta:
    model = Additional_document
    fields = ('user', 'title', 'file')

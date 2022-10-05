from telnetlib import DO
from django.shortcuts import render

from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import (
  UserSerializer,
  RegisterSerializer, 
  DocumentSerializer, 
  AddDocSerializer
)
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics, permissions, parsers, status
from .permissions import IsOwnerOrReadOnly, IsAdminOrReadOnly
from .models import User, Document, Additional_document
from app import serializers


class UserDetail(generics.ListAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  # permission_classes = (IsAdminUser,)

class RegisterUserAPIView(generics.CreateAPIView):
  permission_classes = (AllowAny,)
  serializer_class = RegisterSerializer

class DocumentsView(APIView):
  permission_classes = (IsAuthenticatedOrReadOnly,)
  parser_classes = (parsers.FileUploadParser,)

  def get(self, request, ):
    documents = Document.objects.all()
    serializer = DocumentSerializer(documents, many=True)
    print(serializer.data)
    return Response(serializer.data)

  def post(self, request, *args, **kwargs):
      print(request.data)
      f = request.data['file']
      print(f)
      # serializer = DocumentSerializer(data=request.FILES)
      # print(serializer.is_valid())
      # if serializer.is_valid():
      #   serializer.save()
      #   return Response(serializer.data)


class AddDocView(APIView):
  # serializer_class = AddDocSerializer
  def get(self, request, *args, **kwargs):
    print(request.user)
    documents = Add.objects.all()
    print(documents)
    serializer = AddDocSerializer(documents)
    print(serializer.data)
    return Response({"status":"done"})


# class AddDocView(generics.ListAPIView):
#   serializer_class = AddDocGetSerializer
#   queryset = Additional_documents.objects.all()






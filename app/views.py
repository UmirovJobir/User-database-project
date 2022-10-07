from django.shortcuts import render

from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import (
  AddDocGetSerializer,
  UserSerializer,
  RegisterSerializer, 
  DocumentGetSerializer,
  DocumentPostSerializer,
  AddDocPostSerializer,
  AddDocGetSerializer
)
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics, permissions, parsers, status
from .permissions import IsOwnerOrReadOnly, IsAdminOrReadOnly
from .models import User, Document, Additional_document
from django.http import Http404


class UserDetail(generics.ListAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  # permission_classes = (IsAdminUser,)

class RegisterUserAPIView(generics.CreateAPIView):
  permission_classes = (AllowAny,)
  serializer_class = RegisterSerializer




class DocumentsView(APIView):
  def get(self, request):
    documents = Document.objects.all()
    serializer = DocumentGetSerializer(documents, many=True)
    return Response(serializer.data)

  def post(self, request):
      serializer = DocumentPostSerializer(data=request.data, context={'request': request})
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DocumentsDetailView(APIView):
    permission_classes = (IsOwnerOrReadOnly,)

    def get_object(self, pk):
          try:
              return Document.objects.get(pk=pk)
          except Document.DoesNotExist:
              raise Http404

    def get(self, request, pk, format=None):
          document = self.get_object(pk)
          serializer = DocumentGetSerializer(document)
          return Response(serializer.data)

    def put(self, request, pk, format=None):
          print(request.user.id)
          document = self.get_object(pk)
          serializer = DocumentPostSerializer(document, data=request.data, context={'request': request}, partial=True)
          if serializer.is_valid():
              serializer.save()
              return Response(serializer.data)
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
          document = self.get_object(pk)
          document.delete()
          return Response(status=status.HTTP_204_NO_CONTENT)


class AddDocView(APIView):
    def get(self, request):
      documents = Additional_document.objects.all()
      serializer = AddDocGetSerializer(documents, many=True)
      return Response(serializer.data)

    def post(self, request):
        serializer = AddDocPostSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
          serializer.save()
          return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AddDocDetailView(APIView):
    permission_classes = (IsOwnerOrReadOnly,)
    def get_object(self, pk):
          try:
              return Additional_document.objects.get(pk=pk)
          except Document.DoesNotExist:
              raise Http404

    def get(self, request, pk, format=None):
          document = self.get_object(pk)
          serializer = AddDocGetSerializer(document)
          return Response(serializer.data)

    def put(self, request, pk, format=None):
          document = self.get_object(pk)
          serializer = AddDocPostSerializer(document, data=request.data, context={'request': request}, partial=True)
          if serializer.is_valid():
              serializer.save()
              return Response(serializer.data)
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
          document = self.get_object(pk)
          document.delete()
          return Response(status=status.HTTP_204_NO_CONTENT)






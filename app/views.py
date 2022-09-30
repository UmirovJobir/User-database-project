from django.shortcuts import render

from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import (
  UserSerializer,
  RegisterSerializer, 
  PostCreateSerializer,
  PostGetSerializer, 
  CategorySerializer
)
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics, permissions
from .permissions import IsOwnerOrReadOnly, IsAdminOrReadOnly
from .models import User, Post, Category


class UserDetail(generics.ListAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  permission_classes = (IsAdminUser,)

class RegisterUserAPIView(generics.CreateAPIView):
  permission_classes = (AllowAny,)
  serializer_class = RegisterSerializer


class CategoryView(generics.ListCreateAPIView):
  serializer_class = CategorySerializer
  queryset = Category.objects.all()


class PostGetView(generics.ListAPIView):
  serializer_class = PostGetSerializer
  queryset = Post.objects.all()

class PostCreateView(generics.CreateAPIView):
  serializer_class = PostCreateSerializer
  queryset = Post.objects.all()

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = PostCreateSerializer
  queryset = Post.objects.all()
  # permission_classes = permissions.IsAdminUser




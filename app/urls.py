from .models import User
from django.urls import path, include
from .views import (
  UserDetail,
  RegisterUserAPIView,
  PostGetView,
  PostCreateView,
  PostDetailView,
  CategoryView,
  UserDetail
  )

urlpatterns = [
  path("user", UserDetail.as_view()),
  path("get-details/",UserDetail.as_view()),
  path('register/',RegisterUserAPIView.as_view()),
  path('category/', CategoryView.as_view()),
  path('post_get/', PostGetView.as_view()),
  path('post_create/', PostCreateView.as_view()),
  path('post_detail/<int:pk>/', PostDetailView.as_view()),
  path('drf-auth/', include('rest_framework.urls'))
]
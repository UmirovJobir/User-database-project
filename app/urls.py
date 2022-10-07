from .models import User
from django.urls import path, include, re_path
from .views import (
  UserDetail,
  RegisterUserAPIView,
  DocumentsView,
  AddDocView,
  DocumentsDetailView
  )

urlpatterns = [
  path('register/',RegisterUserAPIView.as_view()),
  path("users", UserDetail.as_view()),
  path('document/', DocumentsView.as_view()),
  path('document/<int:pk>/', DocumentsDetailView.as_view()),
  path('add_doc/', AddDocView.as_view()),

  path('drf-auth/', include('rest_framework.urls')),
]
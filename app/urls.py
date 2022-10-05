from .models import User
from django.urls import path, include, re_path
from .views import (
  UserDetail,
  RegisterUserAPIView,
  DocumentsView,
  AddDocView
  )

urlpatterns = [
  path("user", UserDetail.as_view()),
  path("get-details/",UserDetail.as_view()),
  path('register/',RegisterUserAPIView.as_view()),
  # path('document/', DocumentsView.as_view()),
  path('drf-auth/', include('rest_framework.urls')),
  re_path(r'^document/$', DocumentsView.as_view(), name='document'),
]
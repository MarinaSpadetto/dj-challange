from django.db.models import query
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Author, Article
from django.contrib.auth.models import User
from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import AuthorSerializer, ArticleSerializerLogged, ArticleSerializerAnonymous, UserSerializer


class SignUpViewSet(generics.CreateAPIView):
    """
    Sign up View.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny, )


class AuthorViewSet(viewsets.ModelViewSet):
    """
    Author View.
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    """
    Article View.
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = Article.objects.all()
    serializer_class = ArticleSerializerLogged
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category',]


class ArticlesViewSet(generics.ListAPIView):
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.AllowAny]
    queryset = Article.objects.all()
    serializer_class = ArticleSerializerAnonymous
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category',]

    def get_queryset(self):
        """
        Check if user is Authenticated.
        """

        if self.request.user.is_authenticated:
            self.serializer_class = ArticleSerializerLogged

        return self.queryset
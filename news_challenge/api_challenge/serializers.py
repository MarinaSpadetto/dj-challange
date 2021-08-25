from rest_framework import serializers
from .models import Author, Article
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class AuthorSerializer(serializers.ModelSerializer):
    """
    Author Serializer.
    """

    class Meta:
        model = Author
        fields = ['id', 'name', 'picture']


class ArticleSerializerLogged(serializers.ModelSerializer):
    """
    Article Serializer Logged User.
    """
    class Meta:
        model = Article
        fields = ['id', 'author', 'category', 'title', 'summary', 'firstParagraph', 'body']


class ArticleSerializerAnonymous(serializers.ModelSerializer):
    """
    Article Serializer Anonymous User.
    """
    class Meta:
        model = Article
        fields = ['id', 'author', 'category', 'title', 'summary', 'firstParagraph']


class UserSerializer(serializers.ModelSerializer):
    """
    User Serializer.
    """

    class Meta:
        model = User
        fields = ['username', 'password']
    
    def create(self, validated_data):
        """
        Create a new user with a token authentication.
        :param validated_data: data.
        :return: object user.
        """

        # remove the password from the validated_data and set it on method set_password.
        password = validated_data.pop('password')

        user = User(**validated_data)
        user.set_password(password)
        user.save()

        # create a token for user.
        token = Token.objects.create(user=user)
        token.save()

        return user
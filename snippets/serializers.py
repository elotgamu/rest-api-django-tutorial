from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Snippet


class SnippetSerializer(serializers.ModelSerializer):
    """docstring for SnippetSerializer"""
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Snippet
        fields = ('id',
                  'title',
                  'code',
                  'linenos',
                  'language',
                  'style',
                  'owner'
                  )


class UserSerializer(serializers.ModelSerializer):
    """docstring for UserSerializer"""
    snippets = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'snippets')

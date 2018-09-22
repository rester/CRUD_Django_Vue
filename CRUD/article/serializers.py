"""Module to serializable objects.
"""
from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    """ Class to serialize article models with Meta. Meta reference to other class inner this class.
    """
    class Meta:
        model = Article
        fields = '__all__'

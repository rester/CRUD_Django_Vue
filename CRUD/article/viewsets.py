"""Module of viewsets. Class similar to 'Controllers' or 'Resourses'.
Deal with object to be view from serializabe.
"""
from rest_framework import viewsets, filters
from .models import Article
from .serializers import ArticleSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    """ Responsable to query the object.
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('article_id', 'article_heading', 'article_body')

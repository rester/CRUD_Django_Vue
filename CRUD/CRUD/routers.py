""" Module to implements custom routes of app.
"""
from rest_framework import routers
from article.viewsets import ArticleViewSet

router = routers.DefaultRouter()
router.register(r'article', ArticleViewSet)

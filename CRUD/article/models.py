"""
high level support for doing this and that.
"""
from django.db import models

# Create your models here.
class Article(models.Model):
    """Class that holds model database of article.
    Atributtes:
    - article_id = primary key of the model.
    - article_heading = Title of article.
    - article_body = Text body of the article.
    """
    article_id = models.AutoField(primary_key=True)
    article_heading = models.CharField(max_length=250)
    article_body = models.TextField()

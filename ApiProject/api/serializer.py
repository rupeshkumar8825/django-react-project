# this is serializer for the django project for this purpose 
from rest_framework import serializers;
from .models import Article;

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article;
        fields = ['id', 'title', 'description'];


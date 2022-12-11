# this is serializer for the django project for this purpose 
from rest_framework import serializers;
from .models import Article;


# here we are defining the serializer for the class article which will serialize the data into 
# proper format to be able to read and access the fields in proper manner 
class ArticleSerializer(serializers.ModelSerializer):
    # defining the meta class in order to tell what do we want to be show 
    class Meta:
        # assigning the model to the model of the article that we have made 
        model = Article;
        # here we are giving the fields that we want to serialize
        # in this case we want to show the id, title, and description for this purpose 
        fields = ['id', 'title', 'description'];


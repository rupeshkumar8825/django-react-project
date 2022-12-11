from django.db import models

# Create your models here.
# making our first models in the django project 
class Article(models.Model):
    # we want to make the few fields 
    title = models.CharField(max_length=100);
    description = models.TextField();
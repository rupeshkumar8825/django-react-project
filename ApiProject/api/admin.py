from django.contrib import admin
from .models import Article;
# Register your models here.
# here we have to register our models in order to view this in the admin panel for this purpose 
admin.site.register(Article);
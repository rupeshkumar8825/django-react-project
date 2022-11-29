from django.shortcuts import render
from django.shortcuts import HttpResponse;
from .models import Article;
from .serializer import ArticleSerializer;
from django.http import JsonResponse;
from rest_framework.parsers import JSONParser;
from django.views.decorators.csrf import csrf_exempt;
# Create your views here.
# creating the first view function here 
def index(request):
    return HttpResponse("It is working");


@csrf_exempt
def articleList(request):
    if(request.method == "GET"):
        # here we want to fetch all the articles present in the database 
        articles = Article.objects.all();

        # then we have to serialize this data before sending the json response 
        serilaizer = ArticleSerializer(articles, many=True);

        # now we have to return the json response from the django backend to the react frontend for this purpose
        # say everything went fine 
        return JsonResponse(serilaizer.data, safe=False);

    elif(request.method == "POST"):
        # we have to create the new data and insert this into the sqlite data base for this purpose 
        data = JSONParser().parse(request);
        serilaizer = ArticleSerializer(data=data);

        # now checking whether this is valid or not 
        if(serilaizer.is_valid()):
            # then we are saving the content that we got in the data base for this purpose 
            serilaizer.save();
            
            # say everything went fine 
            return JsonResponse(serilaizer.data, status = 201);
        else:
            # we have an error then we will return the error with status code 401
            return JsonResponse(serilaizer.errors,status = 403);


# now we have to define the view for the another api for this purpose 


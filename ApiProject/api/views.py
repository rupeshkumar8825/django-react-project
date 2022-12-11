from django.shortcuts import render
from django.shortcuts import HttpResponse;
from .models import Article;
from .serializer import ArticleSerializer;
from django.http import JsonResponse;
from rest_framework.parsers import JSONParser;
from django.views.decorators.csrf import csrf_exempt;
from rest_framework.decorators import api_view;
from rest_framework.response import Response;
from rest_framework import status;

# Create your views here.
# creating the first view function here 
def index(request):
    return HttpResponse("It is working");


@api_view(['GET', 'POST'])
def articleList(request):
    if(request.method == "GET"):
        # here we want to fetch all the articles present in the database 
        articles = Article.objects.all();

        # then we have to serialize this data before sending the json response 
        serilaizer = ArticleSerializer(articles, many=True);

        # now we have to return the json response from the django backend to the react frontend for this purpose
        # say everything went fine 
        return Response(serilaizer.data);

    elif(request.method == "POST"):
        # we have to create the new data and insert this into the sqlite data base for this purpose 
       
        # print("The post data after parsing is ", data);
        serilaizer = ArticleSerializer(data=request.data);
        # print("The data after the serializing is ", serilaizer);


        # now checking whether this is valid or not 
        if(serilaizer.is_valid()):
            # then we are saving the content that we got in the data base for this purpose 
            serilaizer.save();
            
            # say everything went fine 
            return Response(serilaizer.data, status = status.HTTP_201_CREATED);
        else:
            # we have an error then we will return the error with status code 401
            return Response(serilaizer.errors,status = status.HTTP_400_BAD_REQUEST);


# now we have to define the view for the another api for this purpose 
@api_view(['GET', 'PUT', 'DELETE'])
def articleDetails(request, pk):
    try:
        # we have to first find whether this exists or not 
        # if it exists then fetch otherwise throw an exception 
        article = Article.objects.get(pk = pk);
    except Article.DoesNotExist : 
        return Response(status=status.HTTP_401_UNAUTHORIZED);

    if (request.method == 'GET'):
        # here the article is not in the proper format to be sent to frontend hence we need to serializer it first
        serializer = ArticleSerializer(article);
        print("The JSON response that we are sending to frontend is \n", JsonResponse(serializer.data));

        # this will send the json response to the frontend in the format of json which we can receive in the frontend 
        return Response(serializer.data);

    elif (request.method == 'PUT'):
        # this is to update the article 
        # here first we are fetching the data content from the request object that we have 
        # data = JSONParser().parse(request);
        serilaizer = ArticleSerializer(data=request.data);



        if(serilaizer.is_valid()):
            serilaizer.save();
            return Response(serilaizer.data, status = status.HTTP_201_CREATED);
        else:
            return Response(serilaizer.errors,status = status.HTTP_403_FORBIDDEN);
        
    elif (request.method == 'DELETE'):
        # we have to delete this article 
        article.delete();
        return JsonResponse(status = 201);
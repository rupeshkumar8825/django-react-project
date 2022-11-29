from django.shortcuts import render
from django.shortcuts import HttpResponse;
# Create your views here.
# creating the first view function here 
def index(request):
    return HttpResponse("It is working");
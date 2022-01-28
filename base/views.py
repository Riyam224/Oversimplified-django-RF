from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from django.http import HttpResponse





def index(request):
    return HttpResponse('hi')

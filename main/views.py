from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Enter your JSON here")
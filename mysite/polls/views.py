from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hallo, you're at the polls index!")

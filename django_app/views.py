from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


def home(request):
    context = {}
    return render(request, 'django_app/home.html', context)
# Create your views here.

import random

from django.http import HttpResponse, JsonResponse, HttpRequest
from django.shortcuts import render


def home(request):
    context = {}
    return render(request, 'django_app/home.html', context)


def get_words(count: int) -> str:
    result = ""
    idx = 1
    while True:
        result += random.choice(["Alfa ", "Betta ", "Gamma ", "Omega "])
        if idx == count:
            break
        idx += 1
    return result.strip()


def posts(request) -> JsonResponse:
    list_comprehension1 = [{
        "userId": int(round(x / 10, 0)),
        "id": x,
        "title": get_words(count=1),
        "body": get_words(count=random.randint(3, 7))
    } for x in range(1, 10)]
    return JsonResponse(data=list_comprehension1, safe=False)

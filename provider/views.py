from django.shortcuts import render
from .models import Test
from django.http import JsonResponse

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("This should work.")

def test(request):
    Test.objects.create(
        name="hello"
    )
    test_objs = list(Test.objects.all().values())
    return JsonResponse(test_objs,safe=False)

    
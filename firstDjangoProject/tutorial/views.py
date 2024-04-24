from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    ctx = {"title":"Tende Luxo"}
    return render(request, template_name="home.html", context=ctx)

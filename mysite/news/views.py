from django.shortcuts import render


def index(request):
    return render(request, 'news/index.html')


def single(request):
    return render(request, 'news/single.html')
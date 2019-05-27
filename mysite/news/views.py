from django.shortcuts import render


def index(request):
    title = 'News'
    return render(request, 'news/index.html', {'title': title})


def single(request):
    title = 'This news'
    return render(request, 'news/single.html', {'title': title})
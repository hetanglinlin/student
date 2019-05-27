from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def coursepage(request):
    return render(request, 'courses.html')

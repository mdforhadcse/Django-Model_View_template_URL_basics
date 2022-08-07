from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    dic = {'text': 'This text come from view'}
    return render(request, 'first_app/home.html', context=dic)


def contact(request):
    return HttpResponse("<h1>This is Contact page</h1> <a href='/first_app/'>Home</a> <a "
                        "href='/first_app/about/'>About</a>")


def about(request):
    return HttpResponse("<h1>This is About page</h1> <a href='/first_app/'>Home</a> <a "
                        "href='/first_app/contact/'>Contact</a>")

# Create your views here.

from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the UVA off grounds housing index.")

def show_user(request, name):
    return HttpResponse("You are looking at this user: " % name)

def show_review(request, review_text):
    return HttpResponse("You are looking at this review: " % review_text)


def all1(request):
    return render(request, "home/INDEX.html")
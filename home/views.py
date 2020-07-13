from django.shortcuts import render

def index(request):
    return render(request,'home/home.html')


def signup(request):
    return render(request,'home/signup.html')
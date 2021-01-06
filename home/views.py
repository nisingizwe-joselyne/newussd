from django.shortcuts import render

# Create your views here.
def welcome(request):
    return render(request,'smart.html')
def Home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')

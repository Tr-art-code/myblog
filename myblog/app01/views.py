from django.shortcuts import render, HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Hello World".encode('utf-8'))
def login(request):
    return render(request, "login.html")
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
  # return HttpResponse("Hello world")
  return render(request, 'index.html')

# Methods can have any name
def about(request):
  return HttpResponse("About Page returning")

def contact(request):
  return HttpResponse("Contact Page returning")
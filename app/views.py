from django.shortcuts import render,HttpResponse

# Create your views here.
def dummypoint(request):
    return HttpResponse('Welome to Django')

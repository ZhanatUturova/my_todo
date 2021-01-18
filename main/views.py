from django.shortcuts import render, HttpResponse
from .models import ToDo

# Create your views here.
def homepage(request):
    return render(request, 'index.html')

def test(request):
    todo_list = ToDo.objects.all()
    return render(request, 'test.html', {"todo_list": todo_list})

def go(request):
    return render(request, 'go.html')

def third(request):
    return HttpResponse('This is third test3')

def one(request):
    return render(request, 'one.html')

def two(request):
    return render(request, 'two.html')

def three(request):
    return render(request, 'three.html')
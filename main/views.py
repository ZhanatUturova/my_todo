from django.shortcuts import render, HttpResponse

# Create your views here.
def homepage(request):
    return render(request, 'index.html')

def test(request):
    return render(request, 'test.html')

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
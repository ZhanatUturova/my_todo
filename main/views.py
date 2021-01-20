from django.shortcuts import render, HttpResponse, redirect
from .models import ToDo, Book

# Create your views here.
def homepage(request):
    return render(request, 'index.html')

def test(request):
    todo_list = ToDo.objects.all()
    return render(request, 'test.html', {"todo_list": todo_list})

def add_todo(request):
    form = request.POST
    text = form["todo_text"]
    todo = ToDo(text=text)
    todo.save()
    return redirect(test)

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

def books(request):
    book_list = Book.objects.all()
    return render(request, 'books.html', {"book_list": book_list})

def add_book(request):
    form = request.POST
    title = form["book_title"]
    book_title = Book(title=title)
    book_title.save()

    subtitle = form["book_subtitle"]
    book_subtitle = Book(subtitle=subtitle)
    book_subtitle.save()

    description = form["book_description"]
    book_description = Book(description=description)
    book_description.save()

    price = form["book_price"]
    book_price = Book(price=price)
    book_price.save()

    genre = form["book_genre"]
    book_genre = Book(genre=genre)
    book_genre.save()

    autor = form["book_autor"]
    book_autor = Book(autor=autor)
    book_autor.save()

    year = form["book_year"]
    book_year = Book(year=year)
    book_year.save()
    return redirect(books)
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

def delete_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.delete()
    return redirect(test)

def mark_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite = not todo.is_favorite
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
    subtitle = form["book_subtitle"]
    description = form["book_description"]
    price = form["book_price"]
    genre = form["book_genre"]
    autor = form["book_autor"]
    year = form["book_year"]
    book = Book(title=title, subtitle=subtitle, description=description, price=price, genre=genre, autor=autor, year=year)
    book.save()
    return redirect(books)

def delete_book(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect(books)

def mark_book(request, id):
    book = Book.objects.get(id=id)
    book.is_favorite = not book.is_favorite
    book.save()
    return redirect(books)

def open_book(request, id):
    book_details = Book.objects.filter(id=id)
    return render(request, 'books_detail.html', {"book_list": book_details})

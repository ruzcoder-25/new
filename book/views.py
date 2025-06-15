from django.shortcuts import render, redirect

from book.models import Book, Author


def book_list(request):
    book = Book.objects.all()
    return render(request, 'book/book_list.html', {
        'book': book
    })

def create_book(request):
    book = None
    authors = Author.objects.all()
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        price = request.POST.get('price')
        author_id = request.POST.get('author')
        if title and description and price and author_id:
            book = Book(
                title=title,
                description=description,
                price=price,
                author_id=author_id,
            )
            book.save()
            return redirect('book-list')

    return render(request, 'book/create_book.html',{
        'authors': authors,
        'book': book
    })

def book_detail(request, pk):
    book = Book.objects.get(pk=pk)
    context = {
        'books': book
    }
    return render(request, 'book/book_detail.html',context)


def update_book(request, pk):
    book = Book.objects.get(pk=pk)
    authors = Author.objects.all()
    if request.method == "POST":
        title = request.POST.get('title',book.title)
        description = request.POST.get('description',book.description)
        price = request.POST.get('price',book.price)
        author_id = request.POST.get('author',book.author.id if book.author else None)
        if title and description and price and author_id:
            book.title = title
            book.description = description
            book.price = price
            book.author_id = author_id
            book.save()
            return redirect('book-list')
    return render(request, 'book/update_book.html',{
        'book': book,
        'authors': authors,
    })


def delete_book(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect('book-list')
    return render(request, 'book/delete_book.html',{'book': book})


# author cruds

def author_list(request):
    author = Author.objects.all()
    return render(request, 'author/author_list.html', {'author': author})


def create_author(request):
    author = None
    if request.method == "POST":
        full_name = request.POST.get('full_name')
        birthday = request.POST.get('birthday')
        country = request.POST.get('country')
        if full_name and birthday and country:
            author = Author(
                full_name=full_name,
                birthday=birthday,
                country=country
            )
            author.save()
            return redirect('author-list')
    return render(request, 'author/creatte_author.html',{'author': author,})


def author_detail(request, pk):
    author = Author.objects.get(pk=pk)
    return render(request, 'author/author_detail.html', {'author': author})


def author_update(request, pk):
    author = Author.objects.get(pk=pk)
    if request.method == "POST":
        full_name = request.POST.get('full_name',author.full_name)
        birthday = request.POST.get('birthday',author.birthday)
        country = request.POST.get('country',author.country)
        if full_name and birthday and country:
            author.full_name = full_name
            author.birthday = birthday
            author.country = country
            author.save()
            return redirect('author-list')
    return render(request, 'author/author_update.html',{'author': author,})


def delete_author(request, pk):
    author = Author.objects.get(pk=pk)
    if request.method == "POST":
        author.delete()
        return redirect('author-list')
    return render(request, 'author/delete_author.html',{'author': author,})
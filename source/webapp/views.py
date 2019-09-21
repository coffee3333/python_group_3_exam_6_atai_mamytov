from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Books
from webapp.forms import BookForm, SearchForm


def index_view(request, *args, **kwargs):
    books = Books.objects.filter(status="active").order_by("-created_at")
    return render(request, 'index.html', context={
        'books': books
    })


def book_create_view(request, *args, **kwargs):
    if request.method == 'GET':
        form = BookForm()
        return render(request, 'create.html', context={'form': form})
    elif request.method == 'POST':
        form = BookForm(data=request.POST)
        if form.is_valid():
            Books.objects.create(
                name_author=form.cleaned_data['name_author'],
                mail_author=form.cleaned_data['mail_author'],
                entry=form.cleaned_data['entry']
            )
            return redirect('index')
        else:
            return render(request, 'create.html', context={'form': form})


def book_edit_view(request, pk):
    book = get_object_or_404(Books, pk=pk)
    if request.method == 'GET':
        form = BookForm(data={
            'name_author' : book.name_author,
            'mail_author' : book.mail_author,
            'entry' : book.entry
        })
        return render(request, 'update.html', context={'form': form, 'book': book})
    elif request.method == 'POST':
        form = BookForm(data=request.POST)
        if form.is_valid():
            book.name_author = request.POST.get('name_author')
            book.mail_author = request.POST.get('mail_author')
            book.entry = request.POST.get('entry')
            book.save()
            return redirect('index')
        else:
            return render(request, 'update.html', context={'book': book, 'form': form})
    return redirect('index')


def book_delete_view(request, pk):
    book = get_object_or_404(Books, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete.html', context={'book': book})
    elif request.method == 'POST':
        book.delete()
        return redirect('index')


def book_search_view(request, *args, **kwargs):
    form = SearchForm(data=request.GET)
    if form.is_valid():
        text = form.cleaned_data['search']
        books = Books.objects.filter(name_author__contains=text, status="active").order_by("-created_at")
        print(text)
        print(books)
        return render(request, 'index.html', context={'books': books})
    else:
        redirect('index')

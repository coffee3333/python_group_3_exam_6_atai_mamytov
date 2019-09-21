from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render
from webapp.models import Books
from webapp.forms import BookForm


def index_view(request, *args, **kwargs):
    books = Books.objects.filter(status="Active").order_by("-created_at")
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
        form = BookForm()
        return render(request, 'update.html', context={'book': book,'form': form})
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
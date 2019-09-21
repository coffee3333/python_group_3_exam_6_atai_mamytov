from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render
from webapp.models import Books
from webapp.forms import BookForm


def index_view(request, *args, **kwargs):
    books = Books.objects.filter(status="Active").order_by("-changed_at")
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
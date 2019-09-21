from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render
from webapp.models import Books


def index_view(request, *args, **kwargs):
    books = Books.objects.filter(status="Active").order_by("-changed_at")
    return render(request, 'index.html', context={
        'books': books
    })
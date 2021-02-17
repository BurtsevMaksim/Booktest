from django.shortcuts import render
from books.serializers import BookSerializer
from rest_framework import viewsets
from books.models import Book


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


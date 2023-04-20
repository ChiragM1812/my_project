from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'author', 'language', 'genre', 'publisher', 'min_age', 'price', 'stock', 'description']
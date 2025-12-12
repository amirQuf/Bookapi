from django.http import JsonResponse
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer



def available_books(request):
    books = Book.objects.filter(is_available=True)
    data = [{"title": b.title, "author": b.author} for b in books]
    return JsonResponse({"books": data})

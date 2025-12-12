from django.test import TestCase
from rest_framework.test import APITestCase
from book.models import Book
from django.urls import reverse 
from datetime import date
from .factories import BookFactory
class  BookApiTest(APITestCase):
    
    def setUp(self):
        self.url = reverse("book-list")
        self.books = BookFactory.create_batch(2)
        

    def test_get_all_books(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()),2)
        
    def test_create_book(self):
        payload = {
            "title": "New Book",
            "author": "Someone",
            "published_date": "2023-01-01",
            "is_available": True
        }
        response  = self.client.post(self.url , payload, format= 'json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Book.objects.count(),3)
        self.assertEqual(Book.objects.last().title, "New Book")
        
    def test_validation_error(self):
        payload =  {
            "author": "Someone",
            "published_date": "2023-01-01",
            "is_available": True
        }
        
        response  = self.client.post(self.url,payload , format = 'json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('title', response.json())
        
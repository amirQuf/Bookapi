from django.test import TestCase
from django.urls import reverse
from datetime import date 
from .factories import BookFactory

class TestAvailableBooksView(TestCase):
    
    
    def setUp(self):
        self.url = reverse("available_books")
        BookFactory(  title="Book A",
            author="Author A",
            published_date=date(2020, 1, 1),
            is_available=True)
        
        BookFactory(
            title="Book B",
            author="Author B",
            published_date=date(2021, 2, 2),
            is_available=False
        )
    def get_response(self):
        ''' helper function '''
        return self.client.get(self.url)
    
    def test_status_code(self):
        response =self.get_response()
        assert response.status_code == 200 
        
    def test_json_structure(self):
        response = self.get_response()
        data = response.json()
        assert 'books' in  data
        assert  isinstance(data["books"] ,list)
        
    def test_filtering_available_books(self):
        response  = self.get_response()
        books = response.json()['books']
        assert len(books) ==1 
        assert books[0]['title'] == "Book A"
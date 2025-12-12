from django.test import TestCase
from ..models import Book
from datetime import date 
from .factories import BookFactory
class BookModelTest(TestCase):
    
    
    def setUp(self):
        '''
        Docstring for setUp
        
        :param self: Description
        '''
        self.book = BookFactory(
        title="Dune",
        author="Frank",
        published_date=date(1965, 1, 1)
    )
        
    def test_str_method(self):
        '''
        Docstring for test_str_method
        
        :param self: Description
        '''
        assert str(self.book) == "Dune by Frank"
   
   
    def test_mark_unavailable(self):
        '''
        Docstring for test_mark_unavailable
        
        :param self: Description
        '''
        self.book.mark_unavailable()
        self.book.refresh_from_db()
        assert self.book.is_available is False


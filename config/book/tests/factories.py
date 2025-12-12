
from book.models import Book
import factory 

class BookFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Book
    
    title = factory.Sequence(lambda n: f"Book {n}")
    author = factory.Faker("name")
    published_date = factory.Faker("date_object")
    is_available = True
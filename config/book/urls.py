from django.urls import path 
from .views import BookViewSet , available_books

from rest_framework.routers import DefaultRouter


urlpatterns = [
path('available',available_books , name= "available_books")
]

router  = DefaultRouter()
router.register('book',BookViewSet)

urlpatterns += router.urls


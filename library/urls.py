from django.urls import path
from .views import *

urlpatterns = [
    path('books/<str:roll>/', GetBooks.as_view()),
]
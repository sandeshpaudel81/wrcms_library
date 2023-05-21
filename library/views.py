from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from .models import BookIssued, Student
from rest_framework import status
import pytz
from rest_framework import serializers

class IssuedBookSerializer(serializers.ModelSerializer):
    book_number = serializers.SerializerMethodField(read_only=True)
    book_name = serializers.SerializerMethodField(read_only=True)
    issued_date = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = BookIssued
        fields = ['id', 'book_name', 'book_number', 'issued_date']

    def get_book_name(self, obj):
        return obj.book.name
    
    def get_book_number(self, obj):
        return obj.book.bookNumber
    
    def get_issued_date(self, obj):
        date = obj.issuedDate.strftime("%d %B %Y")
        return date


class GetBooks(APIView):

    def get(self, request, roll, format=None):
        student = Student.objects.get(rollNumber=roll)
        issuedBooks = BookIssued.objects.filter(student=student, returned=False)
        serializer = IssuedBookSerializer(issuedBooks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

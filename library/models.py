from django.db import models

# Create your models here.
class Student(models.Model):
    rollNumber = models.CharField(max_length=12)
    name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name+' - '+self.rollNumber

class Book(models.Model):
    name = models.CharField(max_length=1024)
    bookNumber = models.CharField(max_length=6)

    def __str__(self):
        return self.name+' - '+self.bookNumber

class BookIssued(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    returned = models.BooleanField(default=False)
    issuedDate = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.student.name+' - '+self.book.name
from django.db import models
from django.contrib.auth.models import User


class Member(models.Model):
    
    name=models.CharField(max_length=200)
    phone=models.CharField(max_length=15)
    address=models.TextField(max_length=300)
    created_date=models.DateField(auto_now_add=True)

    @property
    def rented_books(self):
        return Rent.objects.filter(member=self).order_by("-id")

    def __str__(self):
        return self.name


class Genre(models.Model):

    title=models.CharField(max_length=150)

    def __str__(self):
        return self.title
    
class Author(models.Model):

    name=models.CharField(max_length=200)
    bio=models.TextField(max_length=300)

    def __str__(self):
        return self.name

class Book(models.Model):

    title=models.CharField(max_length=200)
    author=models.ForeignKey(Author, on_delete=models.CASCADE)
    genre=models.ForeignKey(Genre, on_delete=models.CASCADE)
    created_date=models.DateField(auto_now_add=True)
    status=models.BooleanField(default=True)

    @property
    def rent_details(self):
        return Rent.objects.filter(book=self).order_by("-id")
    
    @property
    def current_renter(self):
        return Rent.objects.filter(book=self,return_status=False)

    def __str__(self):
        return self.title
    
class Rent(models.Model):

    book=models.ForeignKey(Book, on_delete=models.CASCADE)
    member=models.ForeignKey(Member, on_delete=models.CASCADE)
    created_date=models.DateField(auto_now_add=True)
    due_date=models.DateField()
    return_date=models.DateField(null=True)
    return_status=models.BooleanField(default=False)
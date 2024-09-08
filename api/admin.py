from django.contrib import admin
from .models import Author,Book,Member,Rent,Genre

admin.site.register(Book)
admin.site.register(Member)
admin.site.register(Rent)
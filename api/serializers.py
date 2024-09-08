from rest_framework import serializers
from .models import Author,Book,Member,Rent,Genre


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:

        model=Author

        fields="__all__"

        read_only_fields=['id']


class GenreSerializer(serializers.ModelSerializer):

    class Meta:

        model=Genre

        fields="__all__"

        read_only_fields=['id']


class RentSerializer(serializers.ModelSerializer):

    book=serializers.StringRelatedField(read_only=True)

    member=serializers.StringRelatedField(read_only=True)

    class Meta:

        model=Rent

        fields="__all__"

        read_only_fields=['id','created_date','return_date','return_status']


class RentSerializer2(serializers.ModelSerializer):

    class Meta:

        model=Rent

        fields="__all__"

        read_only_fields=['id','created_date','return_date','return_status']


class BookSerializer(serializers.ModelSerializer):

    author=serializers.StringRelatedField(read_only=True)

    genre=serializers.StringRelatedField(read_only=True)
    
    rent_details=RentSerializer(many=True,read_only=True)

    current_renter=RentSerializer(many=True,read_only=True)

    class Meta:

        model=Book

        fields="__all__"

        read_only_fields=['id','created_date']

class BookSerializer2(serializers.ModelSerializer):

    rent_details=RentSerializer(many=True,read_only=True)

    current_renter=RentSerializer(many=True,read_only=True)

    class Meta:

        model=Book

        fields="__all__"

        read_only_fields=['id','created_date']


class MemberSerializer(serializers.ModelSerializer):

    rented_books=RentSerializer(many=True,read_only=True)

    class Meta:

        model=Member

        fields="__all__"

        read_only_fields=['id','created_date']
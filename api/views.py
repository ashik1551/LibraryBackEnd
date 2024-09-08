from django.shortcuts import render
from .models import Author,Book,Member,Rent,Genre
from .serializers import AuthorSerializer,BookSerializer,MemberSerializer,RentSerializer,GenreSerializer,BookSerializer2,RentSerializer2
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView,RetrieveUpdateAPIView,RetrieveAPIView
from rest_framework import permissions,status
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from datetime import date


class MemberListCreateView(ListCreateAPIView):

    permission_classes=[permissions.IsAdminUser]

    authentication_classes=[JWTAuthentication]

    serializer_class=MemberSerializer

    queryset=Member.objects.all()

class MemberRetrieveView(RetrieveAPIView):

    permission_classes=[permissions.IsAdminUser]

    authentication_classes=[JWTAuthentication]

    serializer_class=MemberSerializer

    queryset=Member.objects.all()


class AuthorModelViewSetView(ModelViewSet):

    permission_classes=[permissions.IsAdminUser]

    authentication_classes=[JWTAuthentication]

    serializer_class=AuthorSerializer

    queryset=Author.objects.all()


class GenreModelViewSetView(ModelViewSet):

    permission_classes=[permissions.IsAdminUser]

    authentication_classes=[JWTAuthentication]

    serializer_class=GenreSerializer

    queryset=Genre.objects.all()


class BookListCreateView(ListCreateAPIView):

    permission_classes=[permissions.IsAdminUser]

    authentication_classes=[JWTAuthentication]

    serializer_class=BookSerializer

    def list(self, request, *args, **kwargs):
        
        qs=Book.objects.all()

        if 'status' in  request.query_params:

            status1=request.query_params.get('status')

            qs=qs.filter(status=status1)

        if 'author' in request.query_params:

            author=request.query_params.get('author')

            qs=qs.filter(author=author)

        if 'genre' in request.query_params:

            genre=request.query_params.get('genre')

            qs=qs.filter(genre=genre)

        serializer=BookSerializer(qs,many=True)

        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def create(self, request, *args, **kwargs):
        
        authorid=request.query_params.get('author')

        genreid=request.query_params.get('genre')

        author=Author.objects.get(id=authorid)

        genre=Genre.objects.get(id=genreid)

        serializer=BookSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save(author=author,genre=genre)

            return Response(serializer.data,status=status.HTTP_200_OK)
        else:

            return Response(serializer.errors,status=status.HTTP_406_NOT_ACCEPTABLE)
        

class BookRetrieveUpdateDelete(RetrieveUpdateDestroyAPIView):

    permission_classes=[permissions.IsAdminUser]

    authentication_classes=[JWTAuthentication]

    serializer_class=BookSerializer2

    queryset=Book.objects.all()
    
    def update(self, request, *args, **kwargs):
        
        qs=Book.objects.get(id=kwargs.get('pk'))

        authorid=request.query_params.get('author')

        genreid=request.query_params.get('genre')

        author=Author.objects.get(id=authorid)

        genre=Genre.objects.get(id=genreid)

        serializer=BookSerializer(data=request.data,instance=qs)

        if serializer.is_valid():

            serializer.save(author=author,genre=genre)

            return Response(serializer.data,status=status.HTTP_200_OK)
        
        else:

            return Response(serializer.errors,status=status.HTTP_406_NOT_ACCEPTABLE)

       
class RentListCreateView(ListCreateAPIView):

    permission_classes=[permissions.IsAdminUser]

    authentication_classes=[JWTAuthentication]

    serializer_class=RentSerializer

    def list(self, request, *args, **kwargs):
        
        qs=Rent.objects.all().order_by("-id")

        if 'return_status' in request.query_params:

            qs=qs.filter(return_status=request.query_params.get('return_status'))

        serializer=RentSerializer(qs,many=True)

        return Response(serializer.data,status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):

        bookid=request.query_params.get('book')
        
        memberid=request.query_params.get('member')

        book=Book.objects.get(id=bookid)

        member=Member.objects.get(id=memberid)

        serializer=RentSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save(member=member,book=book)

            book.status=False

            book.save()

            return Response(serializer.data,status=status.HTTP_200_OK)
        
        else:

            return Response(serializer.errors,status=status.HTTP_406_NOT_ACCEPTABLE)
        
        
class RentUpdateView(RetrieveUpdateAPIView):

    permission_classes=[permissions.IsAdminUser]

    authentication_classes=[JWTAuthentication]

    serializer_class=RentSerializer2

    queryset=Rent.objects.all()

    def update(self, request, *args, **kwargs):

        qs=Rent.objects.get(id=kwargs.get('pk'))
        
        qs.return_status=True

        qs.return_date=date.today()

        qs.book.status=True

        qs.save()

        qs.book.save()

        serializer=RentSerializer(qs)

        return Response(serializer.data,status=status.HTTP_200_OK)

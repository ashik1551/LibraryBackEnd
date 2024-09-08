from django.urls import path
from api import views
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register('author',views.AuthorModelViewSetView,basename='author')
router.register('genre',views.GenreModelViewSetView,basename='genre')

urlpatterns=[
    path('member/',views.MemberListCreateView.as_view()),
    path('member/<int:pk>/',views.MemberRetrieveView.as_view()),
    path('token/',TokenObtainPairView.as_view()),
    path('token/refresh/',TokenRefreshView.as_view()),
    path('book/',views.BookListCreateView.as_view()),
    path('book/<int:pk>/',views.BookRetrieveUpdateDelete.as_view()),
    path('rent/',views.RentListCreateView.as_view()),
    path('rent/<int:pk>/',views.RentUpdateView.as_view()),
] + router.urls
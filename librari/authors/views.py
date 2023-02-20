from rest_framework import generics
from rest_framework.viewsets import ModelViewSet, ViewSet
from .models import Author, Book, Article, Biography
from .serializers import AuthorModelSerializer, BookModelSerializer, BiographyModelSerializer, ArticleModelSerializer, \
    AuthorModelSerializer2
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import AllowAny


class AuthorPaginator(LimitOffsetPagination):
    default_limit = 10


class AuthorModelViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer
    #filterset_fields = ['first_name', 'last_name', 'birthday_year']
    #pagination_class = AuthorPaginator


class BookModelViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer


class BiographyModelViewSet(ModelViewSet):
    queryset = Biography.objects.all()
    serializer_class = BiographyModelSerializer


class ArticleModelViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleModelSerializer


class MyAPIView(generics.ListAPIView):
        queryset = Author.objects.all()
        serializer = AuthorModelSerializer

        def get_serializer_class(self):
            if self.request.version == '1':
                return AuthorModelSerializer
            return AuthorModelSerializer2


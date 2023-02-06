from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Author, Book, Article, Biography


class Author(HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class Biography(HyperlinkedModelSerializer):
    class Meta:
        model = Biography
        fields = '__all__'


class Article(HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class Book(HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from book.models import Author
from book.models import Book
from book.serializers import AuthorSerializer
from book.serializers import BookSerializer

print(__file__)


class AuthorViewSet(ViewSet):

    def list(self, request):
        queryset = Author.objects.all()
        serializer = AuthorSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = Author.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = AuthorSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = Author.objects.get(pk=pk)
        except Author.DoesNotExist:
            return Response(status=404)
        serializer = AuthorSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = Author.objects.get(pk=pk)
        except Author.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class BookViewSet(ViewSet):

    def list(self, request):
        queryset = Book.objects.all()
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = Book.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = BookSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Response(status=404)
        serializer = BookSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


def test(request):
    pass


error = test
email_book = test
home = test

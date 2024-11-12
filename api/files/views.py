from django.http import HttpResponse
from django.shortcuts import render

from rest_framework import viewsets

from files.models import FileInfo
from files.serializers import FileInfoSerializer


class FileInfoSet(viewsets.ModelViewSet):

    queryset = FileInfo.objects.all()
    serializer_class = FileInfoSerializer


def test(request):
    return HttpResponse("test")

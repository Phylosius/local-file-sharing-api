from django.http import HttpResponse
from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from files.models import FileInfo
from files.serializers import FileInfoSerializer


class FileInfoSet(viewsets.ModelViewSet):

    queryset = FileInfo.objects.all()
    serializer_class = FileInfoSerializer
    permission_classes = (IsAuthenticated, )
    filterset_fields = ['upload_date', 'size']
    search_fields = ['name']


def test(request):
    return HttpResponse("test")

from rest_framework import serializers

from files.models import FileInfo


class FileInfoSerializer(serializers.ModelSerializer):

    class Meta:

        model = FileInfo
        fields = '__all__'


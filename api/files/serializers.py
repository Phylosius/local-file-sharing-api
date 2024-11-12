from rest_framework import serializers

from files.models import FileInfo


class FileInfoSerializer(serializers.ModelSerializer):

    uploadDate = serializers.DateTimeField(source='upload_date')

    class Meta:

        model = FileInfo
        # fields = '__all__'
        exclude = ['upload_date']


from rest_framework import serializers
from .models import Album, Image

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id','path','title','description')

class AlbumSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many = True, read_only = True)
    class Meta:
        model = Album
        fields = ('id','title','description','images')
from rest_framework import serializers
from rest_framework.fields import ImageField

from .models import Works, Pictures


class PicturesSerializer(serializers.ModelSerializer):

    mPic = serializers.ReadOnlyField(source='mobileCompressPic.url')
    compPic = serializers.ReadOnlyField(source='compressPic.url')
    webPic = serializers.ReadOnlyField(source='webPic.url')
    mWebPic = serializers.ReadOnlyField(source='mobileWebPic.url')

    class Meta:
        model = Pictures
        fields = ['pic', 'mPic', 'compPic' ,'webPic', 'mWebPic']


class WorksSerializer(serializers.ModelSerializer):
    mCompPic = serializers.ReadOnlyField(source='mainCompressPic.url')
    webCompPic = serializers.ReadOnlyField(source='webMainCompressPic.url')

    class Meta:
        model = Works
        fields = ['id', 'mainPic', 'mCompPic', 'webCompPic', 'name' ,'descriptions']

class SingleWorksSerializer(serializers.ModelSerializer):
    picture = PicturesSerializer(many=True, read_only=True)
    mCompPic = serializers.ReadOnlyField(source='mainCompressPic.url')
    webCompPic = serializers.ReadOnlyField(source='webMainCompressPic.url')

    class Meta:
        model = Works
        fields = ['id', 'mainPic', 'mCompPic', 'webCompPic', 'name', 'descriptions', 'picture']

class UpdateWorkImageSerializer(serializers.ModelSerializer):
    picture_url = serializers.SerializerMethodField()
    class Meta:
        model = Works
        fields = ['mainPic', 'picture_url']

    def update(self, instance, validated_data):
        instance.mainPic = validated_data.get('mainPic')
        instance.save()
        return instance

    def get_picture_url(self, Works):
        photo_url = Works.mainPic.url
        return photo_url

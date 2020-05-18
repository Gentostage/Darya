from rest_framework import serializers
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


class WorksPOSTSerializer(serializers.ModelSerializer):
    class Meta:
        model = Works
        fields = ['name', 'descriptions']

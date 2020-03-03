from rest_framework import serializers
from .models import Works, Pictures


class PicturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pictures
        fields = ['pic']


class WorksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Works
        fields = ['id', 'mainPic', 'name']

class SingleWorksSerializer(serializers.ModelSerializer):
    picture = PicturesSerializer(many=True, read_only=True)
    class Meta:
        model = Works
        fields = ['id', 'mainPic', 'name', 'descriptions', 'picture']


class WorksPOSTSerializer(serializers.ModelSerializer):
    class Meta:
        model = Works
        fields = ['name', 'descriptions']

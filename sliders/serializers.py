from rest_framework import serializers
from .models import Slider

class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = ['id', 'title', 'url', 'description', 'image']
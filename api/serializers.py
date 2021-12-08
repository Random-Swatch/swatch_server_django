from rest_framework import serializers


class ColorSerializer(serializers.Serializer):
    type = serializers.CharField(max_length=10)
    syntax = serializers.CharField(max_length=50)
    is_css_compatible = serializers.BooleanField()

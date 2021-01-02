from rest_framework import serializers


class dictionary(serializers.Serializer):
    title = serializers.CharField(max_length=100000)
    A = serializers.CharField(max_length=1000)
    B = serializers.CharField(max_length=1000)
    C = serializers.CharField(max_length=1000)
    D = serializers.CharField(max_length=1000)
    sol = serializers.CharField(max_length=1000)
    explanation = serializers.CharField(max_length=10000)
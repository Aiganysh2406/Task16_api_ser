from rest_framework import serializers
from .models import Vaccina

class VaccinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vaccina
        fields = '__all__'

    def validate_title(self, value):
        if len(value) > 30:
            raise ValueError('title lenght more than 30')
        return value
    def validate(self, attrs):
        self.validate_title(attrs['title'])
        return super().validate(attrs)



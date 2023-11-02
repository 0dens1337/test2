from rest_framework import serializers
from .models import ESblog


class ESblogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ESblog
        fields = ('title', 'cat_id')

from django.core.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from .models import Lang

class LangSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lang
        fields = '__all__'

class Item(APIView):
    def get(self, request, id, *args, **kwargs):
        try:
            item = Lang.objects.get(id=id)
            return Response({
                'level_choices': item.LANG_LEVEL_CHOICES,
                'name': item.name,
                'level': item.level,
                'justification': item.justification,
            }, status=status.HTTP_200_OK)
        except Lang.DoesNotExist:
            return Response({'error': 'Lang not found'}, status=status.HTTP_404_NOT_FOUND)

class Items(APIView):
    def get(self, request, *args, **kwargs):
        try:
            data = []
            langs = Lang.objects.all()
            for item in langs:
                data.append({
                    'id': item.id,
                    'name': item.name,
                    'level': item.level,
                })
            return Response(data, status=status.HTTP_200_OK)
        except Lang.DoesNotExist:
            return Response({'error': 'Lang not found'}, status=status.HTTP_404_NOT_FOUND)
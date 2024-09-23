from django.core.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from .models import Title
from core.constants import TITLE_TYPE_CHOICES

class TitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Title
        fields = '__all__'

class Type(APIView):
    def get(self, request, *args, **kwargs):
        try:
            title = Title.objects.get_or_create(id=1)[0]
            data = {
                "type_choices": TITLE_TYPE_CHOICES,
                "type": title.type,
            }
            return Response(data, status=status.HTTP_200_OK)
        except Title.DoesNotExist:
            return Response({'error': 'Title not found'}, status=status.HTTP_404_NOT_FOUND)

class TitleDetails(APIView):
    def get(self, request, *args, **kwargs):
        try:
            title = Title.objects.get_or_create(id=1)[0]
            data = {
                "title": title.title,
                "details": title.details,
            }
            return Response(data, status=status.HTTP_200_OK)
        except Title.DoesNotExist:
            return Response({'error': 'Title not found'}, status=status.HTTP_404_NOT_FOUND)

class Links(APIView):
    def get(self, request, *args, **kwargs):
        try:
            title = Title.objects.get_or_create(id=1)[0]
            data = {
                "linkedin_url": title.linkedin_url,
                "other_url": title.other_url,
                "trimoji_url": title.trimoji_url,
            }
            return Response(data, status=status.HTTP_200_OK)
        except Title.DoesNotExist:
            return Response({'error': 'Title not found'}, status=status.HTTP_404_NOT_FOUND)
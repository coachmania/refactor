from django.core.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Title

class Type(APIView):
    def get(self, request, *args, **kwargs):
        try:
            title = Title.objects.get_or_create(id=1)[0]
            fields = ["type"]
            data = {field: getattr(title, field) for field in fields}
            data["type_choices"] = [choice[1] for choice in Title.TYPE_CHOICES]
            return Response(data, status=status.HTTP_200_OK)
        except Title.DoesNotExist:
            return Response({'error': 'Title not found'}, status=status.HTTP_404_NOT_FOUND)

class TitleDetails(APIView):
    def get(self, request, *args, **kwargs):
        try:
            title = Title.objects.get_or_create(id=1)[0]
            fields = ["title", "details"]
            data = {field: getattr(title, field) for field in fields}
            return Response(data, status=status.HTTP_200_OK)
        except Title.DoesNotExist:
            return Response({'error': 'Title not found'}, status=status.HTTP_404_NOT_FOUND)

class Links(APIView):
    def get(self, request, *args, **kwargs):
        try:
            title = Title.objects.get_or_create(id=1)[0]
            fields = ["linkedin_url", "other_url", "trimoji_url"]
            data = {field: getattr(title, field) for field in fields}
            return Response(data, status=status.HTTP_200_OK)
        except Title.DoesNotExist:
            return Response({'error': 'Title not found'}, status=status.HTTP_404_NOT_FOUND)

class Fields(APIView):
    def put(self, request, *args, **kwargs):
        try:
            title = Title.objects.get_or_create(id=1)[0]
            for key, value in request.data.items():
                setattr(title, key, value)
            try:
                title.save()
            except ValidationError as error:
                return Response(error.message_dict, status=status.HTTP_400_BAD_REQUEST)
            return Response({'success': 'Title updated'}, status=status.HTTP_200_OK)
        except Title.DoesNotExist:
            return Response({'error': 'Title not found'}, status=status.HTTP_404_NOT_FOUND)
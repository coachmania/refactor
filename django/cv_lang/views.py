from django.core.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Lang

class Item(APIView):
    def get(self, request, lang_id, *args, **kwargs):
        try:
            lang = Lang.objects.get(id=lang_id)
            return Response({
                'id': lang.id,
                'name': lang.name,
                'level': lang.level,
                'justification': lang.justification,
            }, status=status.HTTP_200_OK)
        except Lang.DoesNotExist:
            return Response({'error': 'Lang not found'}, status=status.HTTP_404_NOT_FOUND)

class Items(APIView):
    def get(self, request, *args, **kwargs):
        try:
            data = []
            langs = Lang.objects.all()
            for lang in langs:
                data.append({
                    'id': lang.id,
                    'name': lang.name,
                })
            return Response(data, status=status.HTTP_200_OK)
        except Lang.DoesNotExist:
            return Response({'error': 'Lang not found'}, status=status.HTTP_404_NOT_FOUND)

class Fields(APIView):
    def put(self, request, lang_id, *args, **kwargs):
        try:
            lang = Lang.objects.get_or_create(id=lang_id)[0]
            for key, value in request.data.items():
                setattr(lang, key, value)
            try:
                lang.save()
            except ValidationError as error:
                return Response(error.message_dict, status=status.HTTP_400_BAD_REQUEST)
            return Response({'success': 'Lang updated'}, status=status.HTTP_200_OK)
        except Lang.DoesNotExist:
            return Response({'error': 'Lang not found'}, status=status.HTTP_404_NOT_FOUND)
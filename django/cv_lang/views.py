from django.core.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Lang

class Add(APIView):
    def post(self, request, *args, **kwargs):
        try:
            Lang.objects.create(
                name="Nouvelle Langue"
            )
            return Response({'success': 'Lang added'}, status=status.HTTP_201_CREATED)
        except ValidationError as error:
            return Response(error.message_dict, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class Item(APIView):
    def get(self, request, lang_id, *args, **kwargs):
        try:
            lang = Lang.objects.get(id=lang_id)
            return Response({
                'level_choices': lang.LANG_LEVEL_CHOICES,
                'name': lang.name,
                'level': lang.level,
                'justification': lang.justification,
            }, status=status.HTTP_200_OK)
        except Lang.DoesNotExist:
            return Response({'error': 'Lang not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, lang_id, *args, **kwargs):
        try:
            lang = Lang.objects.get(id=lang_id)
            lang.delete()
            return Response({'success': 'Lang deleted'}, status=status.HTTP_204_NO_CONTENT)
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
                    'level': lang.level,
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
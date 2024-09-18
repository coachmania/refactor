from django.core.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Lang

class Add(APIView):
    def post(self, request, *args, **kwargs):
        try:
            Lang.objects.create()
            return Response({'success': 'Lang added'}, status=status.HTTP_201_CREATED)
        except ValidationError as error:
            return Response(error.message_dict, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

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

    def delete(self, request, id, *args, **kwargs):
        try:
            item = Lang.objects.get(id=id)
            item.delete()
            return Response({'success': 'Lang deleted'}, status=status.HTTP_204_NO_CONTENT)
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
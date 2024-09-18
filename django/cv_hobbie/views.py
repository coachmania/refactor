from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Hobbie
from core.constants import HOBBIE_TYPE_CHOICES

class Item(APIView):
    def get(self, request, id, *args, **kwargs):
        try:
            item = Hobbie.objects.get(id=id)
            return Response({
				'type_choices': HOBBIE_TYPE_CHOICES,
                'type': item.type,
				'name': item.name,
				'details': item.details,
				'duration': item.duration,
            }, status=status.HTTP_200_OK)
        except Hobbie.DoesNotExist:
            return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)

class Items(APIView):
    def get(self, request, *args, **kwargs):
        try:
            data = []
            items = Hobbie.objects.all()
            for item in items:
                data.append({
                    'id': item.id,
                    'type': item.type,
                    'name': item.name,
                })
            return Response(data, status=status.HTTP_200_OK)
        except Hobbie.DoesNotExist:
            return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)
from django.core.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Experience
from core.constants import CONTRACT_CHOICES

class Add(APIView):
    def post(self, request, *args, **kwargs):
        try:
            Experience.objects.create()
            return Response({'success': 'Experience added'}, status=status.HTTP_201_CREATED)
        except ValidationError as error:
            return Response(error.message_dict, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class Item(APIView):
    def get(self, request, id, *args, **kwargs):
        try:
            item = Experience.objects.get(id=id)
            return Response({
                'contract_choices': CONTRACT_CHOICES,
                'company': item.company,
                'title': item.title,
                'city': item.city,
                'contract': item.contract,
                'details': item.details,
            }, status=status.HTTP_200_OK)
        except Experience.DoesNotExist:
            return Response({'error': 'Experience not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, id, *args, **kwargs):
        try:
            item = Experience.objects.get(id=id)
            item.delete()
            return Response({'success': 'Experience deleted'}, status=status.HTTP_204_NO_CONTENT)
        except Experience.DoesNotExist:
            return Response({'error': 'Experience not found'}, status=status.HTTP_404_NOT_FOUND)

class Items(APIView):
    def get(self, request, *args, **kwargs):
        try:
            data = []
            items = Experience.objects.all()
            for item in items:
                data.append({
                    'id': item.id,
                    'company': item.company,
                    'title': item.title,
                })
            return Response(data, status=status.HTTP_200_OK)
        except Experience.DoesNotExist:
            return Response({'error': 'Experience not found'}, status=status.HTTP_404_NOT_FOUND)

class Fields(APIView):
    def put(self, request, id, *args, **kwargs):
        try:
            item = Experience.objects.get_or_create(id=id)[0]
            for key, value in request.data.items():
                setattr(item, key, value)
            try:
                item.save()
            except ValidationError as error:
                return Response(error.message_dict, status=status.HTTP_400_BAD_REQUEST)
            return Response({'success': 'Experience updated'}, status=status.HTTP_200_OK)
        except Experience.DoesNotExist:
            return Response({'error': 'Experience not found'}, status=status.HTTP_404_NOT_FOUND)
from django.core.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Experience
from core.constants import MONTH_CHOICES, CONTRACT_CHOICES

class Item(APIView):
    def get(self, request, id, *args, **kwargs):
        try:
            item = Experience.objects.get(id=id)
            return Response({
                'contract_choices': CONTRACT_CHOICES,
                'month_choices': MONTH_CHOICES,
                'company': item.company,
                'title': item.title,
                'city': item.city,
                'contract': item.contract,
                'details': item.details,
                'start_month': item.start_month,
                'start_year': item.start_year,
                'end_month': item.end_month,
                'end_year': item.end_year,
                'is_current': item.is_current,
            }, status=status.HTTP_200_OK)
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
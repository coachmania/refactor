from django.core.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Personnal

from rest_framework.permissions import AllowAny
class Fields(APIView):
    permission_classes = [AllowAny]
    def put(self, request, *args, **kwargs):
        try:
            personnal = Personnal.objects.get_or_create(id=1)[0]
            for key, value in request.data.items():
                setattr(personnal, key, value)
            try:
                personnal.save()
            except ValidationError as error:
                return Response(error.message_dict, status=status.HTTP_400_BAD_REQUEST)
            return Response({'success': 'Personnal updated'}, status=status.HTTP_200_OK)
        except Personnal.DoesNotExist:
            return Response({'error': 'Personnal not found'}, status=status.HTTP_404_NOT_FOUND)
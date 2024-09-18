from django.core.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Personnal
from core.constants import LICENSE_CHOICES
import os, uuid

class Picture(APIView):
    def get(self, request, *args, **kwargs):
        try:
            personnal = Personnal.objects.get_or_create(id=1)[0]
            data = {
                'picture': personnal.picture.url if personnal.picture else None,
                'is_hidden': personnal.is_hidden
            }
            return Response(data, status=status.HTTP_200_OK)
        except Personnal.DoesNotExist:
            return Response({'error': 'Personnal not found'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, *args, **kwargs):
        try:
            personnal = Personnal.objects.get_or_create(id=1)[0]
            if (personnal.picture):
                personnal.picture.delete()
            new_picture = request.FILES['picture']
            extension = os.path.splitext(new_picture.name)[1]
            new_filename = f"{uuid.uuid4()}{extension}"
            new_picture.name = new_filename
            personnal.picture = new_picture
            try:
                personnal.save()
            except ValidationError as error:
                return Response(error.message_dict, status=status.HTTP_400_BAD_REQUEST)
            return Response({'success': 'Picture updated'}, status=status.HTTP_200_OK)
        except Personnal.DoesNotExist:
            return Response({'error': 'Personnal not found'}, status=status.HTTP_404_NOT_FOUND)

class Infos(APIView):
    def get(self, request, *args, **kwargs):
        try:
            personnal = Personnal.objects.get_or_create(id=1)[0]
            data = {
                "first_name": personnal.first_name,
                "name": personnal.name,
                "phone": personnal.phone,
                "email": personnal.email,
                "age": personnal.age,
                "birthdate": personnal.birthdate,
            }
            return Response(data, status=status.HTTP_200_OK)
        except Personnal.DoesNotExist:
            return Response({'error': 'Personnal not found'}, status=status.HTTP_404_NOT_FOUND)

class Address(APIView):
    def get(self, request, *args, **kwargs):
        try:
            personnal = Personnal.objects.get_or_create(id=1)[0]
            data = {
                "additional": personnal.additional,
                "postal_code": personnal.postal_code,
                "city": personnal.city,
                "country": personnal.country,
            }
            return Response(data, status=status.HTTP_200_OK)
        except Personnal.DoesNotExist:
            return Response({'error': 'Personnal not found'}, status=status.HTTP_404_NOT_FOUND) 
            
class Mobility(APIView):
    def get(self, request, *args, **kwargs):
        try:
            personnal = Personnal.objects.get_or_create(id=1)[0]
            data = {
                "license_choices": LICENSE_CHOICES,
                "license": personnal.license,
                "other_license": personnal.other_license,
                "has_vehicle": personnal.has_vehicle,
                "range": personnal.range,
            }
            return Response(data, status=status.HTTP_200_OK)
        except Personnal.DoesNotExist:
            return Response({'error': 'Personnal not found'}, status=status.HTTP_404_NOT_FOUND)
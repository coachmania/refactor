from django.core.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Personnal
import os, uuid

class Picture(APIView):
    def get(self, request, *args, **kwargs):
        try:
            personnal = Personnal.objects.get_or_create(id=1)[0]
            return Response({
                'picture': personnal.picture.url if personnal.picture else None,
                'is_hidden': personnal.is_hidden
            }, status=status.HTTP_200_OK)
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
            fields = ["first_name", "name", "phone", "email", "age", "birthdate"]
            data = {field: getattr(personnal, field) for field in fields}
            return Response(data, status=status.HTTP_200_OK)
        except Personnal.DoesNotExist:
            return Response({'error': 'Personnal not found'}, status=status.HTTP_404_NOT_FOUND)

class Address(APIView):
    def get(self, request, *args, **kwargs):
        try:
            personnal = Personnal.objects.get_or_create(id=1)[0]
            fields = ["additional", "postal_code", "city", "country"]
            data = {field: getattr(personnal, field) for field in fields}
            return Response(data, status=status.HTTP_200_OK)
        except Personnal.DoesNotExist:
            return Response({'error': 'Personnal not found'}, status=status.HTTP_404_NOT_FOUND) 
            
class Mobility(APIView):
    def get(self, request, *args, **kwargs):
        try:
            personnal = Personnal.objects.get_or_create(id=1)[0]
            fields = ["license", "other_license", "has_vehicle", "range"]
            data = {field: getattr(personnal, field) for field in fields}
            data["license_choices"] = Personnal.LICENSE_CHOICES
            return Response(data, status=status.HTTP_200_OK)
        except Personnal.DoesNotExist:
            return Response({'error': 'Personnal not found'}, status=status.HTTP_404_NOT_FOUND)

class Fields(APIView):
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
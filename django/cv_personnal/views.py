from django.core.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Personnal

from rest_framework.permissions import AllowAny
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
            data["license_choices"] = [choice[1] for choice in Personnal.LICENSE_CHOICES]
            return Response(data, status=status.HTTP_200_OK)
        except Personnal.DoesNotExist:
            return Response({'error': 'Personnal not found'}, status=status.HTTP_404_NOT_FOUND)

class Fields(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        try:
            personnal = Personnal.objects.get_or_create(id=1)[0]
            license_choices = [choice[1] for choice in Personnal.LICENSE_CHOICES]
            data = {
                "license_choices": license_choices,
                "name": personnal.name,
                "first_name": personnal.first_name,
                "phone": personnal.phone,
                "email": personnal.email,
                "age": personnal.age,
                "birthdate": personnal.birthdate,
                "additional": personnal.additional,
                "postal_code": personnal.postal_code,
                "city": personnal.city,
                "country": personnal.country,
                "license": personnal.license,
                "other_license": personnal.other_license,
                "has_vehicle": personnal.has_vehicle,
                "range": personnal.range,
            }
            return Response(data, status=status.HTTP_200_OK)
        except Personnal.DoesNotExist:
            return Response({'error': 'Personnal not found'}, status=status.HTTP_404_NOT_FOUND)

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
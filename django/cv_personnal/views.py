from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, serializers
from .models import Personnal

class PersonnalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personnal
        fields = '__all__'

class Fields(APIView):
    def get(self, request, *args, **kwargs):
        try:
            personnal = Personnal.objects.get_or_create(id=1)[0]
            data = {
            }
            return Response(data, status=status.HTTP_200_OK)
        except Personnal.DoesNotExist:
            return Response({'error': 'Personnal not found'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, *args, **kwargs):
        try:
            personnal = Personnal.objects.get_or_create(id=1)[0]
            serializer = PersonnalSerializer(personnal, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'success': 'Personnal updated'}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Personnal.DoesNotExist:
            return Response({'error': 'Personnal not found'}, status=status.HTTP_404_NOT_FOUND)
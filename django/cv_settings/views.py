from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from .models import Settings
from cv.getObjects import getSingleObject
from .schemes import TEMPLATES

class SettingsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Settings
		fields = '__all__'

class Fields(APIView):
	def get(self, request):
		serializer = SettingsSerializer(getSingleObject(request, Settings))
		return Response(serializer.data, status=status.HTTP_200_OK)

class Scheme(APIView):
	def get(self, request, id, *args, **kwargs):
		try:
			scheme = TEMPLATES[id]
			return Response(scheme, status=status.HTTP_200_OK)
		except:
			return Response({'error': 'Color not found'}, status=status.HTTP_404_NOT_FOUND)
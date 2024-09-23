from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from .models import Settings
from cv.getObjects import getSingleObject

class SettingsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Settings
		fields = '__all__'

class Fields(APIView):
	def get(self, request):
		serializer = SettingsSerializer(getSingleObject(request, Settings))
		return Response(serializer.data, status=status.HTTP_200_OK)
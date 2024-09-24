from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, serializers, status
from .models import Settings
from cv.getObjects import getSingleObject
from .schemes import TEMPLATES
from .sizes import SIZES

class SettingsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Settings
		fields = '__all__'

class SettingsListCreateView(generics.ListCreateAPIView):
    queryset = Settings.objects.all()
    serializer_class = SettingsSerializer

class SettingsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Settings.objects.all()
    serializer_class = SettingsSerializer

class Fields(APIView):
	def get(self, request):
		serializer = SettingsSerializer(getSingleObject(request, Settings))
		data = dict(serializer.data)
		data['sizes'] = SIZES
		return Response(data, status=status.HTTP_200_OK)

class Scheme(APIView):
	def get(self, request, id, *args, **kwargs):
		try:
			scheme = TEMPLATES[id]
			return Response(scheme, status=status.HTTP_200_OK)
		except:
			return Response({'error': 'Color not found'}, status=status.HTTP_404_NOT_FOUND)
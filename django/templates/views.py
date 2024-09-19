from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .schemes import TEMPLATES

class Scheme(APIView):
	def get(self, request, id, *args, **kwargs):
		try:
			scheme = TEMPLATES[id]
			return Response(scheme, status=status.HTTP_200_OK)
		except:
			return Response({'error': 'Color not found'}, status=status.HTTP_404_NOT_FOUND)
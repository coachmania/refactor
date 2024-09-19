from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Cv
from .getDatas import getPersonnalData, getLangData
from cv_personnal.models import Personnal
from cv_lang.models import Lang

from rest_framework.permissions import AllowAny	
class Content(APIView):
	permission_classes = [AllowAny]

	def get(self, request, id, *args, **kwargs):
		try:
			data = {
				'personnal': getPersonnalData(request, Personnal),
				'langs': getLangData(request, Lang),
			}
			return Response(data, status=status.HTTP_200_OK)
		except Cv.DoesNotExist:
			return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)
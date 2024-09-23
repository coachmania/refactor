from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Cv
from .getDatas import getPersonnalData, getTitleData, getLangData, getExperienceData, getSettingsData
from cv_personnal.models import Personnal
from cv_title.models import Title
from cv_lang.models import Lang
from cv_experience.models import Experience

class Content(APIView):
	def get(self, request, *args, **kwargs):
		try:
			data = {
				'personnal': getPersonnalData(request, Personnal),
				'title': getTitleData(request, Title),
				'langs': getLangData(request, Lang),
				'experiences': getExperienceData(request, Experience),
			}
			return Response(data, status=status.HTTP_200_OK)
		except Cv.DoesNotExist:
			return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)
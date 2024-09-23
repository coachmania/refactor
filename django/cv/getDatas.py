from .getObjects import getSingleObject, getMultipleObjects
from cv_personnal.views import PersonnalSerializer
from cv_title.views import TitleSerializer
from cv_lang.views import LangSerializer
from cv_experience.views import ExperienceSerializer

def getPersonnalData(request, model):
	serializer = PersonnalSerializer(getSingleObject(request, model))
	return serializer.data

def getTitleData(request, model):
	serializer = TitleSerializer(getSingleObject(request, model))
	return serializer.data

def getLangData(request, model):
	serializer = LangSerializer(getMultipleObjects(request, model), many=True)
	return serializer.data

def getExperienceData(request, model):
	serializer = ExperienceSerializer(getMultipleObjects(request, model), many=True)
	return serializer.data
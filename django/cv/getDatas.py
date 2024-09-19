from .getObjects import getSingleObject, getMultipleObjects
from cv_personnal.views import PersonnalSerializer
from cv_lang.views import LangSerializer

def getPersonnalData(request, model):
	serializer = PersonnalSerializer(getSingleObject(request, model))
	return serializer.data

def getLangData(request, model):
	serializer = LangSerializer(getMultipleObjects(request, model), many=True)
	return serializer.data
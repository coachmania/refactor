from .getObjects import getSingleObject
from cv_personnal.views import PersonnalSerializer

def getPersonnalData(request, model):
	serializer = PersonnalSerializer(getSingleObject(request, model))
	return serializer.data
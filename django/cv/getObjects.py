from .models import Cv

def getCvObject(request):
	"""
	Get the current CV of the user.
	"""
	user = request.user
	# TODO
	# if user.current_cv:
		# return user.current_cv
	cv, created = Cv.objects.get_or_create(user=request.user, id=1)
	if created:
		user.current_cv = cv
		user.save()
	return cv

def getSingleObject(request, model):
	"""
	Used only for single objects (Title, Personnal, Settings).
	"""
	cv = getCvObject(request)
	try:
		object = model.objects.get_or_create(cv=cv)[0]
	except model.DoesNotExist:
		object = None
	return object

def getMultipleObjects(request, model):
	"""
	Get all objects from the database directly with the right CV associated.
	"""
	cv = getCvObject(request)
	try :
		objects = model.objects.filter(cv=cv)
	except model.DoesNotExist:
		objects = None
	return objects
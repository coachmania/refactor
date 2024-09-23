from django.db import models
from cv.models import Cv

class Settings(models.Model):
	cv = models.OneToOneField(Cv, on_delete=models.CASCADE, related_name='settings')
	# template = models.ForeignKey(Template, on_delete=models.CASCADE, related_name='settings', default=1)
	# experience_first = models.BooleanField(default=True)
	primary_color = models.CharField(max_length=7, blank=True)
	secondary_color = models.CharField(max_length=7, blank=True)
	third_color = models.CharField(max_length=7, blank=True)
	dark_color = models.CharField(max_length=7, blank=True)
	light_color = models.CharField(max_length=7, blank=True)
	# size = models.CharField(max_length=50, blank=True, default=SIZE_OPTIONS[1])
	
	# TODO faire une view qui envoie tout le contenu pour le cv
	# uen fois que le cv le recois (CurrentTemplate) on stocke ce contenu dans pinia 
	# a chauqe fields quon change on update au serveur et au pinia  
from django.db import models
from cv.models import Cv
from core.constants import TITLE_TYPE_CHOICES

class Title(models.Model):
	cv = models.OneToOneField(Cv, on_delete=models.CASCADE, related_name='title')
	type = models.CharField(max_length=50, blank=True, default=TITLE_TYPE_CHOICES[0])
	title = models.CharField(max_length=100, blank=True)
	details = models.CharField(max_length=1000, blank=True)
	# TODO enlever max_lenght et mettre des URLField au lieu de CharField
	linkedin_url = models.CharField(max_length=100, blank=True)
	other_url = models.CharField(max_length=100, blank=True)
	trimoji_url = models.CharField(max_length=100, blank=True)
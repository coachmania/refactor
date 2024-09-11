from django.db import models
from model_utils import Choices

class Title(models.Model):
	TYPE_CHOICES = Choices(
		('Emploi', 'Emploi'),
		('Alternance', 'Alternance'),
		('Stage', 'Stage'),
	)
	# cv = models.OneToOneField(Cv, on_delete=models.CASCADE, related_name='title')
	type = models.CharField(max_length=50, blank=True, choices=TYPE_CHOICES, default=TYPE_CHOICES.Emploi)
	title = models.CharField(max_length=100, blank=True)
	details = models.CharField(max_length=1000, blank=True)
	linkedin_url = models.URLField(blank=True)
	other_url = models.URLField(blank=True)
	trimoji_url = models.URLField(blank=True)
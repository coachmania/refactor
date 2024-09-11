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
	# TODO enlever max_lenght et mettre des URLField au lieu de CharField
	linkedin_url = models.CharField(max_lenght=100, blank=True)
	other_url = models.CharField(max_lenght=100, blank=True)
	trimoji_url = models.CharField(max_lenght=100, blank=True)
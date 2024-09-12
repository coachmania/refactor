from django.core.exceptions import ValidationError
from django.db import models
from model_utils import Choices
import re

class EmailField(models.CharField):
	def clean(self, value, model_instance):
		if value:
			if not re.match(r"[^@]+@[^@]+\.[^@]+", value):
				raise ValidationError("L'email n'est pas valide")
		return value

class AgeField(models.PositiveIntegerField):
	def clean(self, value, model_instance):
		if value in [None, '']:
			return None
		try:
			value = int(value)
		except (ValueError, TypeError):
			raise ValidationError("Veuillez entrer un âge valide sous forme de nombre.")
		if value < 0 or value > 150:
			raise ValidationError("L'âge doit être compris entre 0 et 150.")
		return value

class DateField(models.CharField):
	def clean(self, value, model_instance):
		if len(value) != 10:
			raise ValidationError("La date doit être au format JJ-MM-AAAA")
		return value

class Personnal(models.Model):
	LICENSE_CHOICES = Choices(
		('Aucun', 'Aucun'),
		('BSR', 'BSR'),
		('Permis A', 'Permis A'),
		('Permis B', 'Permis B'),
		('Autre', 'Autre')
	)

	# cv = models.OneToOneField(Cv, on_delete=models.CASCADE, related_name='personnal')
	# profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True, default="")
	# original_picture = models.ImageField(upload_to='original_pictures/', null=True, blank=True, default="")
	is_hidden = models.BooleanField(default=False)
	name = models.CharField(max_length=50, blank=True)
	first_name = models.CharField(max_length=50, blank=True)
	phone = models.CharField(max_length=20, blank=True)
	email = EmailField(max_length=254, blank=True)
	age = AgeField(null=True)
	birthdate = DateField(max_length=10, blank=True)
	additional = models.CharField(max_length=50, blank=True)
	# postal_code = PostalCodeField(null=True)
	city = models.CharField(max_length=50, blank=True)
	country = models.CharField(max_length=50, blank=True)
	license = models.CharField(max_length=50, choices=LICENSE_CHOICES, default=LICENSE_CHOICES.Aucun)
	other_license = models.CharField(max_length=50, blank=True)
	has_vehicle = models.BooleanField(default=False)
	range = models.CharField(max_length=100, blank=True)

	def save(self, *args, **kwargs):
		self.full_clean()
		super().save(*args, **kwargs)
from django.core.exceptions import ValidationError
from django.db import models
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

class PostalCodeField(models.PositiveIntegerField):
	def clean(self, value, model_instance):
		if value in [None, '']:
			return None
		try:
			value = int(value)
		except (ValueError, TypeError):
			raise ValidationError("Le code postal doit être un nombre")
		if len(str(value)) != 5:
			raise ValidationError("Le code postal doit être composé de 5 chiffres")
		return value

class Personnal(models.Model):
	LICENSE_CHOICES = [
		'Aucun',
		'BSR',
		'Permis A',
		'Permis B',
		'Autre'
	]

	# cv = models.OneToOneField(Cv, on_delete=models.CASCADE, related_name='personnal')
	picture = models.ImageField(upload_to='pictures/', null=True, blank=True, default="")
	is_hidden = models.BooleanField(default=False)
	name = models.CharField(max_length=50, blank=True)
	first_name = models.CharField(max_length=50, blank=True)
	phone = models.CharField(max_length=20, blank=True)
	email = EmailField(max_length=254, blank=True)
	age = AgeField(null=True)
	birthdate = DateField(max_length=10, blank=True)
	additional = models.CharField(max_length=50, blank=True)
	postal_code = PostalCodeField(null=True)
	city = models.CharField(max_length=50, blank=True)
	country = models.CharField(max_length=50, blank=True)
	license = models.CharField(max_length=50, default=LICENSE_CHOICES[0])
	other_license = models.CharField(max_length=50, blank=True)
	has_vehicle = models.BooleanField(default=False)
	range = models.CharField(max_length=100, blank=True)

	def save(self, *args, **kwargs):
		self.full_clean()
		super().save(*args, **kwargs)
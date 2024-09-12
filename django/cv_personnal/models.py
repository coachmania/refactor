from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
from django.db import models
from model_utils import Choices
import re

class EmailField(models.CharField):
	default_validators = [EmailValidator(message="Veuillez entrer une adresse email valide.")]

	def validate(self, value, model_instance):
		super().validate(value, model_instance)
		if not re.match(r"[^@]+@[^@]+\.[^@]+", value):
			raise ValidationError("Veuillez entrer une adresse email valide.")
		
class AgeField(models.CharField):
	def to_python(self, value):
		if value in [None, '']:
			return None
		try:
			return int(value)
		except ValueError:
			raise ValidationError("Veuillez entrer un âge valide sous forme de nombre.")

	def validate(self, value, model_instance):
		value = self.to_python(value)
		super().validate(value, model_instance)
		if value is not None and (value < 0 or value > 150):
			raise ValidationError("L'âge doit être compris entre 0 et 150.")

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
	age = AgeField(max_length=3)
	# birthdate = DateField(max_length=10, blank=True)
	additional = models.CharField(max_length=50, blank=True)
	# postal_code = PostalCodeField(null=True)
	city = models.CharField(max_length=50, blank=True)
	country = models.CharField(max_length=50, blank=True)
	license = models.CharField(max_length=50, blank=True, default="Aucun")
	other_license = models.CharField(max_length=50, blank=True)
	has_vehicle = models.BooleanField(default=False)
	range = models.CharField(max_length=100, blank=True)
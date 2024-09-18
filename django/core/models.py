from django.db import models
from django.core.exceptions import ValidationError
from .constants import MONTH_CHOICES

class YearField(models.PositiveIntegerField):
	def clean(self, value, model_instance):
		if type(value) is str:
			if value == "":
				return None
			if not value.isdigit():
				raise ValidationError("L'année doit être un nombre")
			value = int(value)
		return value

class ADateFields(models.Model):
	start_month = models.CharField(max_length=50, blank=True, default=MONTH_CHOICES[0])
	start_year = YearField(null=True)
	end_month = models.CharField(max_length=50, blank=True, default=MONTH_CHOICES[0])
	end_year = YearField(null=True)
	is_current = models.BooleanField(default=False)

	class Meta:
		abstract = True
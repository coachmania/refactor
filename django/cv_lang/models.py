from django.db import models
from model_utils import Choices

class Lang(models.Model):
	LANG_LEVEL_CHOICES = Choices(
		('maternelle', 'Langue maternelle'),
		('B1', 'B1'),
		('B2', 'B2'),
		('C1', 'C1'),
		('C2', 'C2'),
	)
	# cv = models.ForeignKey(Cv, on_delete=models.CASCADE, related_name='langs')
	name = models.CharField(max_length=50, blank=True)
	level = models.CharField(max_length=50, blank=True, choices=LANG_LEVEL_CHOICES, default=LANG_LEVEL_CHOICES.maternelle)
	justification = models.CharField(max_length=100, blank=True)
	order = models.PositiveIntegerField(null=True, blank=True, editable=False)

	def save(self, *args, **kwargs):
		self.full_clean()
		# setOrder(self)
		super().save(*args, **kwargs)
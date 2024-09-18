from django.db import models
from core.models import ADateFields

class Formation(ADateFields):
	# cv = models.ForeignKey(Cv, on_delete=models.CASCADE, related_name='experiences')
	location = models.CharField(max_length=100, blank=True)
	title = models.CharField(max_length=100, blank=True)
	city = models.CharField(max_length=100, blank=True)
	level = models.CharField(max_length=100, blank=True)
	details = models.TextField(blank=True)
	order = models.PositiveIntegerField(null=True, blank=True, editable=False)

	def save(self, *args, **kwargs):
		self.full_clean()
		# setOrder(self)
		super().save(*args, **kwargs)
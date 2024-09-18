from django.db import models
from core.constants import MONTH_CHOICES, CONTRACT_CHOICES

class Experience(models.Model):
	# cv = models.ForeignKey(Cv, on_delete=models.CASCADE, related_name='experiences')
	company = models.CharField(max_length=100, blank=True)
	title = models.CharField(max_length=100, blank=True)
	city = models.CharField(max_length=100, blank=True)
	contract = models.CharField(max_length=50, blank=True, default=CONTRACT_CHOICES[0])
	details = models.TextField(blank=True)
	start_month = models.CharField(max_length=50, blank=True, default=MONTH_CHOICES[0])
	start_year = models.PositiveIntegerField(null=True, blank=True)
	end_month = models.CharField(max_length=50, blank=True, default=MONTH_CHOICES[0])
	end_year = models.PositiveIntegerField(null=True, blank=True)
	order = models.PositiveIntegerField(null=True, blank=True, editable=False)

	def save(self, *args, **kwargs):
		self.full_clean()
		# setOrder(self)
		super().save(*args, **kwargs)

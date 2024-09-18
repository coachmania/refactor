from django.db import models

class Hobbie(models.Model):
	# cv = models.ForeignKey(Cv, on_delete=models.CASCADE, related_name='experiences')
	type = models.CharField(max_length=100, blank=True)
	name = models.CharField(max_length=100, blank=True)
	details = models.TextField(blank=True)
	duration = models.CharField(max_length=100, blank=True)
	order = models.PositiveIntegerField(null=True, blank=True, editable=False)

	def save(self, *args, **kwargs):
		self.full_clean()
		# setOrder(self)
		super().save(*args, **kwargs)
from django.db import models

class Experience(models.Model):
	# cv = models.ForeignKey(Cv, on_delete=models.CASCADE, related_name='experiences')
	company = models.CharField(max_length=100, blank=True)
	title = models.CharField(max_length=100, blank=True)
	city = models.CharField(max_length=100, blank=True)
	contract = models.CharField(max_length=50, blank=True, default="")
	details = models.TextField(blank=True)
	order = models.PositiveIntegerField(null=True, blank=True, editable=False)
	is_open = models.BooleanField(default=False)

	def save(self, *args, **kwargs):
		self.full_clean()
		# setOrder(self)
		super().save(*args, **kwargs)

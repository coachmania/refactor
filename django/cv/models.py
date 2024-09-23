from django.db import models
from django.contrib.auth.models import User

class Cv(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cvs')
	name = models.CharField(max_length=50, blank=True, default="Nouveau CV")
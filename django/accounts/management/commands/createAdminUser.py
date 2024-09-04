from	django.core.management.base import BaseCommand
from	django.contrib.auth import get_user_model
import	os

class Command(BaseCommand):
	help = 'Create admin user'

	def handle(self, *args, **kwargs):
		User = get_user_model()

		username = os.getenv('DJANGO_ADMIN_USERNAME', 'admin')
		email = os.getenv('DJANGO_ADMIN_EMAIL', 'admin@example.com')
		password = os.getenv('DJANGO_ADMIN_PASSWORD', 'adminpassword')

		if not User.objects.filter(username=username).exists():
			User.objects.create_superuser(
				username=username,
				email=email,
				password=password,
			)
			print('Admin user created.')
		else:
			print('Admin user already exists.')
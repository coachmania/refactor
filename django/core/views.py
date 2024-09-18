from django.core.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

SUCCESS_RESPONSE = {'success': 'Item updated'}
ERROR_RESPONSE = {'error': 'Item not found'}

def _saveItems(item, request):
	for key, value in request.data.items():
		setattr(item, key, value)
	try:
		item.save()
	except ValidationError as error:
		return Response(error.message_dict, status=status.HTTP_400_BAD_REQUEST)
	return Response(SUCCESS_RESPONSE, status=status.HTTP_200_OK)

class FieldsSingle(APIView):
	model = None

	def put(self, request, *args, **kwargs):
		try:
			item = self.model.objects.get_or_create(id=1)[0]
			return _saveItems(item, request)
		except self.model.DoesNotExist:
			return Response(ERROR_RESPONSE, status=status.HTTP_404_NOT_FOUND)

class FieldsMultiple(APIView):
	model = None

	def put(self, request, id, *args, **kwargs):
		try:
			item = self.model.objects.get_or_create(id=id)[0]
			return _saveItems(item, request)
		except self.model.DoesNotExist:
			return Response(ERROR_RESPONSE, status=status.HTTP_404_NOT_FOUND)
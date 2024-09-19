from django.core.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from cv.getObjects import getCvObject

SUCCESS_RESPONSE = {'success': 'Item updated'}
DELETE_RESPONSE = {'success': 'Item deleted'}
ERROR_RESPONSE = {'error': 'Item not found'}

def _saveItems(item, request):
	for key, value in request.data.items():
		setattr(item, key, value)
	try:
		item.save()
	except ValidationError as error:
		return Response(error.message_dict, status=status.HTTP_400_BAD_REQUEST)
	return Response(SUCCESS_RESPONSE, status=status.HTTP_200_OK)

class Update(APIView):
	model = None

	def put(self, request, *args, **kwargs):
		try:
			item = self.model.objects.get_or_create(id=1)[0]
			return _saveItems(item, request)
		except self.model.DoesNotExist:
			return Response(ERROR_RESPONSE, status=status.HTTP_404_NOT_FOUND)

class UpdateWithId(APIView):
	model = None

	def put(self, request, id, *args, **kwargs):
		try:
			item = self.model.objects.get_or_create(id=id)[0]
			return _saveItems(item, request)
		except self.model.DoesNotExist:
			return Response(ERROR_RESPONSE, status=status.HTTP_404_NOT_FOUND)

class Add(APIView):
	model = None

	def post(self, request, *args, **kwargs):
		try:
			cv = getCvObject(request)
			self.model.objects.create(cv=cv)
			return Response(SUCCESS_RESPONSE, status=status.HTTP_201_CREATED)
		except ValidationError as error:
			return Response(error.message_dict, status=status.HTTP_400_BAD_REQUEST)
		except Exception as e:
			return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class Delete(APIView):
	model = None

	def delete(self, request, id, *args, **kwargs):
		try:
			item = self.model.objects.get(id=id)
			item.delete()
			return Response(DELETE_RESPONSE, status=status.HTTP_204_NO_CONTENT)
		except self.model.DoesNotExist:
			return Response(ERROR_RESPONSE, status=status.HTTP_404_NOT_FOUND)
from django.core.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class Fields(APIView):
    model = None

    def put(self, request, id, *args, **kwargs):
        try:
            item = self.model.objects.get_or_create(id=id)[0]
            for key, value in request.data.items():
                setattr(item, key, value)
            try:
                item.save()
            except ValidationError as error:
                return Response(error.message_dict, status=status.HTTP_400_BAD_REQUEST)
            return Response({'success': 'Item updated'}, status=status.HTTP_200_OK)
        except self.model.DoesNotExist:
            return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)
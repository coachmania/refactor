from django.core.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Lang

class Fields(APIView):
    def put(self, request, *args, **kwargs):
        try:
            lang = Lang.objects.get_or_create(id=1)[0]
            for key, value in request.data.items():
                setattr(lang, key, value)
            try:
                lang.save()
            except ValidationError as error:
                return Response(error.message_dict, status=status.HTTP_400_BAD_REQUEST)
            return Response({'success': 'Lang updated'}, status=status.HTTP_200_OK)
        except Lang.DoesNotExist:
            return Response({'error': 'Lang not found'}, status=status.HTTP_404_NOT_FOUND)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, serializers
from .models import Title

class TitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Title
        fields = '__all__'

class Type(APIView):
    def get(self, request, *args, **kwargs):
        try:
            # TODO temp replace with cv=cv
            title = Title.objects.get_or_create(id=1)[0]
            type_labels = [choice[1] for choice in Title.TYPE_CHOICES]
            data = {
                'type': title.type,
                'type_choices': type_labels
            }
            return Response(data, status=status.HTTP_200_OK)
        except Title.DoesNotExist:
            return Response({'error': 'Title not found'}, status=status.HTTP_404_NOT_FOUND)

class Details(APIView):
    def get(self, request, *args, **kwargs):
        try:
            title = Title.objects.get_or_create(id=1)[0]
            data = {
                'title': title.title,
                'details': title.details,
            }
            return Response(data, status=status.HTTP_200_OK)
        except Title.DoesNotExist:
            return Response({'error': 'Title not found'}, status=status.HTTP_404_NOT_FOUND)

class Field(APIView):
    def put(self, request, *args, **kwargs):
        try:
            title = Title.objects.get_or_create(id=1)[0]
            serializer = TitleSerializer(title, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'success': 'Title updated'}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Title.DoesNotExist:
            return Response({'error': 'Title not found'}, status=status.HTTP_404_NOT_FOUND)
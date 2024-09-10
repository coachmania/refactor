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

    def put(self, request, *args, **kwargs):
        try:
            title = Title.objects.get_or_create(id=1)[0]
            title.type = request.data['type']
            title.save()
            return Response({'success': 'Title updated'}, status=status.HTTP_200_OK)
        except Title.DoesNotExist:
            return Response({'error': 'Title not found'}, status=status.HTTP_404_NOT_FOUND)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, serializers
from .models import Title

class TitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Title
        fields = '__all__'

class Update(APIView):
    def post(self, request, *args, **kwargs):
        serializer = TitleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# TODO just for test 
from rest_framework.permissions import AllowAny
class Type(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        try:
            # TODO temp
            title = Title.objects.get_or_create(id=1)[0]
            type_labels = [choice[1] for choice in Title.TYPE_CHOICES]
            data = {
                'type': title.type,
                'type_choices': type_labels
            }
            return Response(data, status=status.HTTP_200_OK)
        except Title.DoesNotExist:
            return Response({'error': 'Title not found'}, status=status.HTTP_404_NOT_FOUND)
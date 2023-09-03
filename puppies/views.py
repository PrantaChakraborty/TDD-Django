from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response

from .serializers import PuppySerializer

from .models import Puppy


class PuppyAPIViewSet(ModelViewSet):
    """
    api viewset for puppies
    """
    permission_classes = []
    serializer_class = PuppySerializer
    http_method_names = ['get']

    def get_queryset(self):
        queryset = Puppy.objects.all()
        return queryset

    def list(self, request, *args, **kwargs):
        data = self.get_queryset()
        serializer = self.serializer_class(data, many=True)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)

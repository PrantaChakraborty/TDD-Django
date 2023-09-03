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
    http_method_names = ['get', 'post']

    def get_object(self):
        try:
            puppy_obj = Puppy.objects.get(id=self.kwargs['pk'])
            return puppy_obj
        except Puppy.DoesNotExist:
            return None

    def get_queryset(self):
        queryset = Puppy.objects.all()
        return queryset

    def list(self, request, *args, **kwargs):
        data = self.get_queryset()
        serializer = self.get_serializer(data, many=True)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        puppy_obj = self.get_object()
        if puppy_obj is not None:
            serializer = self.get_serializer(puppy_obj)
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"data": []}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"data": serializer.data}, status.HTTP_201_CREATED)
        else:
            return Response({"data": []}, status=status.HTTP_400_BAD_REQUEST)


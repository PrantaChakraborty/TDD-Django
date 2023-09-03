import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse

from ..models import Puppy
from ..serializers import PuppySerializer


client = Client()


class GetAllPuppiesTest(TestCase):
    """
    testcase to get all the puppies
    """
    def setUp(self) -> None:
        Puppy.objects.create(name='Casper', age=3, breed='Bull Dog', color='Black')
        Puppy.objects.create(name='Muffin', age=1, breed='Gradane', color='Brown')
        Puppy.objects.create(name='Rambo', age=2, breed='Labrador', color='Black')
        Puppy.objects.create(name='Ricky', age=6, breed='Labrador', color='Brown')

    def test_get_puppies(self):
        response = client.get(reverse('puppies-list'))
        puppies = Puppy.objects.all()
        serializer = PuppySerializer(puppies, many=True)
        self.assertEqual(response.data, {"data": serializer.data})   # check the data
        self.assertEqual(response.status_code, status.HTTP_200_OK)

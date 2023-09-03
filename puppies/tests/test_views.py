import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse

from ..models import Puppy
from ..serializers import PuppySerializer


client = Client()


class PuppiesAPIViewSetTest(TestCase):
    """
    testcase to get all the puppies
    """
    def setUp(self) -> None:
        self.casper = Puppy.objects.create(name='Casper', age=3, breed='Bull Dog', color='Black')
        self.muffin = Puppy.objects.create(name='Muffin', age=1, breed='Gradane', color='Brown')
        self.rambo = Puppy.objects.create(name='Rambo', age=2, breed='Labrador', color='Black')
        self.ricky = Puppy.objects.create(name='Ricky', age=6, breed='Labrador', color='Brown')

        self.valid_payload = {
            'name': 'Muffin',
            'age': 4,
            'breed': 'Pamerion',
            'color': 'White'
        }
        self.invalid_payload = {
            'name': '',
            'age': 4,
            'breed': 'Pamerion',
            'color': 'White'
        }

    def test_get_puppies(self):
        response = client.get(reverse('puppies-list'))
        puppies = Puppy.objects.all()
        serializer = PuppySerializer(puppies, many=True)
        self.assertEqual(response.data, {"data": serializer.data})   # check the data
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_single_valid_puppy(self):
        response = client.get(reverse('puppies-detail', kwargs={'pk': self.rambo.pk}))
        puppy = Puppy.objects.get(id=self.rambo.pk)
        serializer = PuppySerializer(puppy)
        self.assertEqual(response.data, {"data": serializer.data})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_single_invalid_puppy(self):
        response = client.get(reverse('puppies-detail', kwargs={'pk': 30}))
        self.assertEqual(response.data, {"data": []})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_valid_puppy(self):
        response = client.post(reverse('puppies-list'),
                               data=json.dumps(self.valid_payload),
                               content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_puppy(self):
        response = client.post(reverse('puppies-list'),
                               data=json.dumps(self.invalid_payload),
                               content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)



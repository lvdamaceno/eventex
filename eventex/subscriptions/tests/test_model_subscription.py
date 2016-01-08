from datetime import datetime

from django.test import TestCase
from eventex.subscriptions.models import Subscription

class SubscritionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='Vinícius Damaceno',
            cpf='12345678901',
            email='lvdamaceno@gmail.com',
            phone='91-908069474'
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())


    def test_created_at(self):
        """Subscription must have an auto created_ad attr."""
        self.assertIsInstance(self.obj.created_at, datetime)



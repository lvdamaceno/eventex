from django.core.exceptions import ValidationError
from django.test import TestCase
from eventex.core.models import Speaker, Contact



class ContactModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker.objects.create(
            name='Vinicius Damaceno',
            slug='vinicius-damaceno',
            photo='http://www.viniciusdamaceno.com.br/static/img/faceofboe.png'
        )

    def test_email(self):
        contact = Contact.objects.create(speaker=self.speaker,kind=Contact.EMAIL,value='lvdamaceno@gmail.com')

        self.assertTrue(Contact.objects.exists())

    def test_phone(self):
        contact = Contact.objects.create(speaker=self.speaker,kind=Contact.PHONE,value='91-980869474')

        self.assertTrue(Contact.objects.exists())

    def test_choices(self):
        """Contact kind should be limited to E or P"""
        contact = Contact(speaker=self.speaker, kind='A', value='B')
        self.assertRaises(ValidationError, contact.full_clean)

    def test_str(self):
        contact = Contact(speaker=self.speaker,kind=Contact.EMAIL,value='lvdamaceno@gmail.com')

        self.assertEqual('lvdamaceno@gmail.com', str(contact))

class ContactManagerTest(TestCase):
    def setUp(self):
        s = Speaker.objects.create(
            name='Vinicius Damaceno',
            slug='vinicius-damaceno',
            photo='http://www.viniciusdamaceno.com.br/static/img/faceofboe.png'
        )

        s.contact_set.create(kind=Contact.EMAIL, value='lvdamaceno@gmail.com')
        s.contact_set.create(kind=Contact.PHONE, value='91-980869474')

    def test_emails(self):
        qs = Contact.objects.emails()
        expected = ['lvdamaceno@gmail.com']
        self.assertQuerysetEqual(qs, expected, lambda o: o.value)

    def test_phones(self):
        qs = Contact.objects.phones()
        expected = ['91-980869474']
        self.assertQuerysetEqual(qs, expected, lambda o: o.value)

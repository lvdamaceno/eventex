from django.test import TestCase
from eventex.core.models import Talk

class TalkModelTest(TestCase):
    def setUp(self):
        self.talk = Talk.objects.create(
            title='Título da Palestra'
        )

    def test_create(self):
        self.assertTrue(Talk.objects.exists())

    def test_has_speakers(self):
        """Talk has many spekaers and vice-versa"""
        self.talk.speakers.create(
            name='Vinícius Damaceno',
            slug='vinicius-damaceno',
            website='http://www.viniciusdamaceno.com.br'
        )
        self.assertEqual(1, self.talk.speakers.count())

    def test_description_blank(self):
        field = Talk._meta.get_field('description')
        self.assertTrue(field.blank)

    def test_speaker_blank(self):
        field = Talk._meta.get_field('speakers')
        self.assertTrue(field.blank)

    def test_start_blank(self):
        field = Talk._meta.get_field('start')
        self.assertTrue(field.blank)

    def test_start_null(self):
        field = Talk._meta.get_field('start')
        self.assertTrue(field.null)

    def test_str(self):
        self.assertEqual('Título da Palestra', str(self.talk))
from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Vinícius Damaceno', cpf='12345678901',
                    email='lvdamaceno@gmail.com', phone='91-98086-9474')
        self.resp = self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'lvdamaceno@gmail.com']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Vinícius Damaceno',
            '12345678901',
            'lvdamaceno@gmail.com',
            '91-98086-9474'
        ]

        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)

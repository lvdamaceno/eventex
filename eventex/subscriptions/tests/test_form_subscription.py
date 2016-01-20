from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm


class SubscriptionFormTest(TestCase):

    def test_has_fiels(self):
        """Form must have 4 fields."""
        form = SubscriptionForm()
        expected = ['name', 'cpf', 'email', 'phone']
        self.assertSequenceEqual(expected, list(form.fields))

    def test_cpf_is_digits(self):
        form = self.make_validated_form(cpf='ABCD5678901')
        #self.assertFormErrorMessage(form, 'cpf', 'CPF deve conter apenas números')
        self.assertFormErrorCode(form, 'cpf', 'digits')

    def test_cpf_has_11_digits(self):
        form = self.make_validated_form(cpf='1234')
        #self.assertFormErrorMessage(form, 'cpf', 'CPF deve ter 11 números.')
        self.assertFormErrorCode(form, 'cpf', 'length')

    def test_name_must_be_captalize(self):
        form = self.make_validated_form(name='VINÍCIUS damaceno')
        self.assertEqual('Vinícius Damaceno', form.cleaned_data['name'])

    def test_email_is_optional(self):
        """email is optional"""
        form = self.make_validated_form(email='')
        self.assertFalse(form.errors)

    def test_phone_is_optional(self):
        """phone is optional"""
        form = self.make_validated_form(phone='')
        self.assertFalse(form.errors)

    def test_musst_inform_email_or_phone(self):
        """email and phone are optional but one must be informed."""
        form = self.make_validated_form(email='',phone='')
        self.assertListEqual(['__all__'], list(form.errors))

    def assertFormErrorCode(self, form, field, code):
        errors = form.errors.as_data()
        errors_list = errors[field]
        exception = errors_list[0]
        self.assertEqual(code, exception.code)


    def assertFormErrorMessage(self, form, field, msg):
        errors = form.errors
        errors_list = errors[field]
        self.assertListEqual([msg], errors_list)


    def make_validated_form(self, **kwargs):
        valid = dict(name='Vinícius Damaceno', cpf='12345678901',
                    email='lvdamaceno@asd.com', phone='91-912345678')
        data = dict(valid, **kwargs)
        form = SubscriptionForm(data)
        form.is_valid()
        return form
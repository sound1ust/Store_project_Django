from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse

from users.forms import UserRegistrationForm


class UserRegistrationViewTestCase(TestCase):
    def setUp(self):
        self.path = reverse('users:registration')

    def test_user_registration_get(self):
        response = self.client.get(self.path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Регистрация')
        self.assertTemplateUsed(response, 'users/registration.html')

    def test_user_registration_post_success(self):
        data = {
            'first_name': 'Pavel', 'last_name': 'Solenik',
            'username': 'pavelsoll2', 'email': 'pavelsoll2@gmail.com',
            'password1': '12345678qQ', 'password2': '12345678qQ',
        }
        response = self.client.post(self.path, data=data)



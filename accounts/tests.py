# from django.test import TestCase
# from django.urls import reverse
# from accounts.forms import CustomUserCreationForm, CustomUserChangeForm
# from django.contrib.auth import get_user_model
#
# User = get_user_model()
#
#
# class CustomUserCreationFormTest(TestCase):
#     def test_valid_form_data(self):
#         form_data = {
#             'username': 'mozhgang',
#             'email': 'mozhgan@test.com',
#         }
#         form = CustomUserCreationForm(data=form_data)
#         self.assertTrue(form.is_valid())
#
#     def test_invalid_form_passwords_not_matching(self):
#         form_data = {
#             'username': 'mozhgang',
#             'email': 'mozhgan@test.com',
#             'password1': 'mozhgang1372',
#             'password2': 'mozhgang1372',
#         }
#         form = CustomUserCreationForm(data=form_data)
#         self.assertFalse(form.is_valid())
#         self.assertIn('password2', form.errors)
#
#
# class CustomUserChangeFormTest(TestCase):
#     def test_valid_form_data(self):
#         form_data = {
#             'username': 'mozhgang',
#             'email': 'mozhgan@test.com',
#         }
#         form = CustomUserChangeForm(data=form_data)
#         self.assertTrue(form.is_valid())
#
#     def test_invalid_form_passwords_not_matching(self):
#         form_data = {
#             'username': 'mozhgang',
#             'email': 'mozhgan@test.com',
#             'password1': 'mozhgang1372',
#             'password2': 'mozhgang1372',
#         }
#         form = CustomUserChangeForm(data=form_data)
#         self.assertFalse(form.is_valid())
#         self.assertIn('password2', form.errors)
#
#
# class SignUpViewTest(TestCase):
#     def test_signup_view_pages_load(self):
#         response = self.client.get(reverse('signup'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'registration/signup.html')
#
#
# class AccountsUrlsTest(TestCase):
#     def setUp(self):
#         self.user = User.objects.create_user(username='mozhgang', password='mozhgang1372')
#
#     def test_signup_url(self):
#         url = reverse('signup')
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'registration/signup.html')

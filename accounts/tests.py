# from django.test import TestCase
#
# from accounts.forms import CustomUserCreationForm, CustomUserChangeForm
# from accounts.models import CustomUser
#
#
# class CustomUserCreationFormTests(TestCase):
#
#     def test_valid_form_creates_user(self):
#         form_data = {
#             'username': 'mozhgang',
#             'email': 'mozhgan@test.com',
#         }
#
#     form = CustomUserCreationForm(data=form_data)
#     self.assertTrue(form.is_valid())
#     user = form.save()
#     self.assertEqual(user.username, 'mozhgang')
#     self.assertEqual(user.email, 'mozhgan@test.com')

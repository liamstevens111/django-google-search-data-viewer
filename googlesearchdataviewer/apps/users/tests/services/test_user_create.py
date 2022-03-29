from django.test import TestCase
from django.core.exceptions import ValidationError

from googlesearchdataviewer.apps.users.models import BaseUser
from googlesearchdataviewer.apps.users.services import user_create


class UserCreateTests(TestCase):
  @classmethod
  def setUpTestData(cls):
      cls.user = user_create(email='random_user@email.com', password='SomePassw0rd12')

  def test_user_with_capitalized_email_cannot_be_created(self):
    with self.assertRaises(ValidationError):
        user_create(
            email='RANDOM_User@Email.Com', password='SomePassw0rd12'
        )

    self.assertEqual(1, BaseUser.objects.count())

from rest_framework.test import APITestCase
from authentication.models import User


class TestModel(APITestCase):

    def test_creates_user(self):
        user=User.objects.create_user('usernametest','usernametest@gmail.com','passwordtest')
        self.assertIsInstance(user,User)
        self.assertEqual(user.email,'usernametest@gmail.com')

    def test_creates_superuser(self):
        user=User.objects.create_superuser('usernametest','usernametest@gmail.com','passwordtest')
        self.assertIsInstance(user,User)
        self.assertEqual(user.email,'usernametest@gmail.com')

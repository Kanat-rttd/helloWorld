from django.test import TestCase
from .models import User


class UserModelTest(TestCase):
    def test_1(self):
        self.assertEqual(1, 1)

    def test_1(self):
        self.assertEqual(2, 2)

    def setUp(self):
        # Create a User instance for testing
        self.user = User.objects.create(name='John Doe', device='Mobile')

    def test_user_creation(self):
        # Test user creation.
        self.assertEqual(self.user.name, 'John Doe')
        self.assertEqual(self.user.device, 'Mobile')

    def test_user_str_method(self):
        # Test the __str__ method of the User model.
        expected_str = "Name: John Doe, Entry device: Mobile"
        self.assertEqual(str(self.user), expected_str)

    def test_user_deletion(self):
        # Test deleting a user
        user_id = self.user.id

        self.user.delete()

        with self.assertRaises(User.DoesNotExist):
            deleted_user = User.objects.get(id=user_id)
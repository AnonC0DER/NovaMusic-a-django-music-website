from django.test import TestCase
from django.contrib.auth import get_user_model

class TestCustomUserModel(TestCase):
    '''Test custom user model'''
    
    def test_create_user_with_email(self):
        '''Test creating a new user with an email is successful'''
        email = 'test@gmail.com'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.is_active)
        self.assertTrue(user.check_password(password))
    
    def test_user_email_normalized(self):
        '''Test the email for a new user is normalized'''
        email = 'test@GmAil.CoM'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )

        self.assertEqual(user.email, email.lower())
    
    def test_user_invalid_email(self):
        '''Test creating user with no email raises error'''
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'testpass123')

    def test_create_superuser_with_email(self):
        '''Test creating a new superuser'''
        user = get_user_model().objects.create_superuser(
            'test@gmail.com',
            'testpass123'
        )

        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_active)

    def test_superuser_invalid_email(self):
        '''Test creating superuser with no email raises error'''
        with self.assertRaises(ValueError):
            get_user_model().objects.create_superuser(None, 'testpass123')
#!/usr/bin/python3
"""
This module contain a class test_User for testing the User
model
"""
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """
    Test the user model
    """

    def __init__(self, *args, **kwargs):
        """Initialize instance variables """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def setUp(self):
        """Create an essentials for every test"""
        self.new = self.value()

    def test_first_name(self):
        """Test the first name"""
        self.new.first_name = "ABC"
        self.assertEqual(self.new.first_name, 'ABC')

    def test_last_name(self):
        """Test last name """
        self.new.last_name = "xyz"
        self.assertEqual(self.new.last_name, 'xyz')

    def test_email(self):
        """Test email """
        self.new.email = "abcxyz@abc.com"
        self.assertEqual(self.new.email, "abcxyz@abc.com")

    def test_password(self):
        """Test password"""
        self.new.password = "abc123"
        self.assertEqual(self.new.password, "abc123")

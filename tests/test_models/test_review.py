#!/usr/bin/python3
"""Test model Review"""
from tests.test_models.test_base_model import test_basemodel
from models.review import Review
from models.place import Place
from models.user import User


class test_review(test_basemodel):
    """Define testcases for Review"""

    def __init__(self, *args, **kwargs):
        """Define instance attributes"""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ """
        new = self.value()
        place = Place()
        new.place_id = place.id
        self.assertEqual(new.place_id, place.id)

    def test_user_id(self):
        """ """
        new = self.value()
        user = User()
        new.user_id = user.id
        self.assertEqual(new.user_id, user.id)

    def test_text(self):
        """ """
        new = self.value()
        new.text = "This is elegant!"
        self.assertEqual(new.text, "This is elegant!")

#!/usr/bin/python3
""" This module contain a testCase instance that tests Amenity
model"""
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """Test Amenity class"""

    def __init__(self, *args, **kwargs):
        """Initialize instance attributes"""
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """Test name"""
        new = self.value()
        new.name = "Hermione"
        self.assertEqual(new.name, "Hermione")

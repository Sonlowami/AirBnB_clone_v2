#!/usr/bin/python3
"""This module tests model Place"""
from tests.test_models.test_base_model import test_basemodel
from models.place import Place
from models.city import City
from models.user import User


class test_Place(test_basemodel):
    """ Test model Place"""

    def __init__(self, *args, **kwargs):
        """Initialize instance attributes"""
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def setUp(self):
        """Create common items"""
        self.new = self.value()

    def test_city_id(self):
        """Test City_id"""
        city = City()
        self.new.city_id = city.id
        self.assertEqual(self.new.city_id, city.id)

    def test_user_id(self):
        """ Test user id"""
        user = User()
        self.new.user_id = user.id
        self.assertEqual(self.new.user_id, user.id)

    def test_name(self):
        """ Test name """
        self.new.name = "Lisbon"
        self.assertEqual(self.new.name, "Lisbon")

    def test_description(self):
        """ Test description"""
        self.new.description = "This is my house"
        self.assertEqual(self.new.description, "This is my house")

    def test_number_rooms(self):
        """Test rooms"""
        self.new.number_rooms = 3
        self.assertEqual(self.new.number_rooms, 3)

    def test_number_bathrooms(self):
        """Test number of bathrooms"""
        self.new.number_bathrooms = 2
        self.assertEqual(self.new.number_bathrooms, 2)

    def test_max_guest(self):
        """Test maximum guests"""
        self.new.max_guest = 2
        self.assertEqual(self.new.max_guest, 2)

    def test_price_by_night(self):
        """Test price per night"""
        self.new.price_by_night = 21
        self.assertEqual(self.new.price_by_night, 21)

    def test_latitude(self):
        """ Test latitude"""
        self.new.latitude = 23.21
        self.assertEqual(self.new.latitude, 23.21)

    def test_longitude(self):
        """Test longitude"""
        self.new.longitude = 2.25
        self.assertEqual(self.new.longitude, 2.25)

    def test_amenity_ids(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)

#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.city import City
from models.state import State


class test_City(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def setUp(self):
        """Create common items for each test"""
        self.new = self.value()

    def test_state_id(self):
        """Test state_id"""
        state = State()
        self.new.state_id = state.id
        self.assertEqual(self.new.state_id, state.id)

    def test_name(self):
        """Test City name"""
        self.new.name = "Lisbon"
        self.assertEqual(self.new.name, "Lisbon")

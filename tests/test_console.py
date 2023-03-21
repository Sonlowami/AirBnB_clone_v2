#!/usr/bin/pyton3

"""
This file contain different tests for the console.py
file
"""
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage
from tests import clear


class TestConsole(unittest.TestCase):
    """
    Test several functionalities of the console
    """

    def test_create_fs(self):
        """ Test if the create feature for the file storage mode"""
        with patch('sys.stdout', new=StringIO()) as mock_out:
            cons = HBNBCommand()
            cons.onecmd("create City name=Cape_Town")
            mocked_id = mock_out.getvalue().strip() # extract the printed id
            self.assertIn("City.{}".format(mocked_id), storage.all().keys())
            clear(mock_out)
            
            cons.onecmd("show City {}".format(mocked_id))
            self.assertIn("'name': 'Cape Town'", mock_out.getvalue().strip())
            clear(mock_out)

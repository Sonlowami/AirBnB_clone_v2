#!/usr/bin/pyton3

"""
This file contain different tests for the console.py
file
"""
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage, storage_mode
from tests import clear
import MySQLdb
import os


class TestConsole(unittest.TestCase):
    """
    Test several functionalities of the console
    """

    @unittest.skipIf(not storage_mode, "Close a connection object")
    def setUp(self):
        """create a setup"""
        self.db = MySQLdb.connect(
                host=os.getenv("HBNB_MYSQL_HOST"),
                user=os.getenv("HBNB_MYSQL_USER"),
                port=3306,
                passwd=os.getenv("HBNB_MYSQL_PWD"),
                db=os.getenv("HBNB_MYSQL_DB")
                )

    @unittest.skipIf(not storage_mode, "Close a connection object")
    def tearDown(self):
        """Close a connection object after every test"""
        self.db.close()

    @unittest.skipIf(storage_mode(), "Database not supported")
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

    @unittest.skipIf(not storage_mode(), "File storage not supported")
    def test_create_db(self):
        """Test if the test feature works well with the database storage"""
        with patch('sys.stdout', new=StringIO()) as mock_out:
            cons = HBNBCommand()
            cons.onecmd("create User email='abcd@gmail.com' password='abcdef' first_name='ab' last_name='cd'")
            mocked_id = mock_out.getvalue().strip()
            clear(mock_out)
            cur = self.db.cursor()
            cur.execute("SELECT * FROM users WHERE id='{}'".format(mocked_id))
            result = cur.fetchone()
            self.assertTrue(result is not None)
            self.assertIn("abcd@gmail.com", result[0])
            self.assertIn("abcdef", result[1])
            cur.close()


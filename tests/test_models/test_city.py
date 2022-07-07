#!/usr/bin/python3

"""
this module defines unittest for models/city.py
Unittest Classe:
"""

import unittest
from models.city import City
from models import city
from models.base_model import BaseModel
import pep8


class TestCity(unittest.TestCase):
    """Unittest for test instantiation of city"""
    @classmethod
    def setUpClass(self):
        my_City = City()

    def test_is_an_instance(self):
        """ Instantiating Citys """
        my_City = City()
        self.assertIsInstance(my_City, City)

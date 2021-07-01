#!/usr/bin/python3
"""
adde comment here
"""
import unittest
import models.amenity
from datetime import datetime


class Test_Amenity(unittest.TestCase):
    """Console methods test"""

    @classmethod
    def setUpClass(self):
        self.amenity1 = models.amenity.Amenity()
        self.amenity2 = models.amenity.Amenity()

    @classmethod
    def tearDownClass(self):
        del self.amenity1
        del self.amenity2

    def test_amenity_update_method(self):
        """check the proper working of the update method"""

        date1 = self.amenity1.updated_at
        self.amenity1.save()
        self.assertNotEqual(self.amenity1.updated_at, date1)

#!/usr/bin/python3
"""
adde comment here
"""
import unittest
import models.city
from datetime import datetime


class Test_City(unittest.TestCase):
    """Console methods test"""

    @classmethod
    def setUpClass(self):
        self.model1 = models.city.City()
        self.model2 = models.city.City()

    @classmethod
    def tearDownClass(self):
        del self.model1
        del self.model2

    def test_city_update_method(self):
        """check the proper working of the update method"""

        date1 = self.model1.updated_at
        self.model1.save()
        self.assertNotEqual(self.model1.updated_at, date1)


if __name__ == '__name__':
    unittest.main()

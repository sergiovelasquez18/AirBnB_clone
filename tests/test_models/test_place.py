#!/usr/bin/python3
"""
adde comment here
"""
import unittest
import models.place
from datetime import datetime


class Test_Place(unittest.TestCase):
    """Console methods test"""

    @classmethod
    def setUpClass(self):
        self.model1 = models.place.Place()
        self.model2 = models.place.Place()

    @classmethod
    def tearDownClass(self):
        del self.model1
        del self.model2

    def test_place_save_method(self):
        """tests proper functionin of save method"""

        date1 = self.model1.updated_at
        self.model1.save()
        self.assertNotEqual(self.model1.updated_at, date1)


if __name__ == '__name__':
    unittest.main()

#!/usr/bin/python3
"""
adde comment here
"""
import unittest
import models.base_model
from datetime import datetime


class Test_BaseModel(unittest.TestCase):
    """Console methods test"""

    @classmethod
    def setUpClass(self):
        self.model1 = models.base_model.BaseModel()
        self.model2 = models.base_model.BaseModel()

    @classmethod
    def tearDownClass(self):
        del self.model1
        del self.model2

    def test_save_method(self):
        """tests proper functionin of save method"""

        date1 = self.model1.updated_at
        self.model1.save()
        self.assertNotEqual(self.model1.updated_at, date1)

    def test_dict__method(self):
        self.assertIsInstance(self.model1.__str__(), str)

if __name__ == '__name__':
    unittest.main()

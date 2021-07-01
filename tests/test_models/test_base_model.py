#!/usr/bin/python3
"""
adde comment here
"""
import unittest
import models.base_model
from datetime import datetime
import os


class Test_BaseModel(unittest.TestCase):
    """Console methods test"""

    @classmethod
    def setUpClass(self):
        """
        creates instances of the class which
        are available whithing this test file
        """
        self.model1 = models.base_model.BaseModel()
        self.model2 = models.base_model.BaseModel()

    @classmethod
    def tearDownClass(self):
        """
        deletes the instances created by setUpClass method at
        the end of the execution of this test
        """
        del self.model1
        del self.model2

    def test_update_method(self):
        """check the proper working of the update method"""
        date1 = self.model1.updated_at
        self.model1.save()
        self.assertNotEqual(self.model1.updated_at, date1)

    def test_dict__method(self):
        """tests the kind of object __self__ methods outputs"""
        self.assertIsInstance(self.model1.__str__(), str)

    def test_save__method(self):
        """tests the kind of object __self__ methods outputs"""
        self.model1.save()
        fileName = r"file.json"
        self.assertTrue((os.path.isfile(fileName)), True)

if __name__ == '__name__':
    unittest.main()

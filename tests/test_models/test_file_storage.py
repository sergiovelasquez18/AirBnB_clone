#!/usr/bin/python3
"""
adde comment here
"""
import unittest
import models.engine.file_storage
from datetime import datetime


class Test_FileStorage(unittest.TestCase):
    """Console methods test"""

    @classmethod
    def setUpClass(self):
        self.model1 = models.engine.file_storage.FileStorage()
        self.model2 = models.engine.file_storage.FileStorage()

    @classmethod
    def tearDownClass(self):
        del self.model1
        del self.model2

    def test_file_storage_save_method(self):
        """tests proper functionin of save method"""

        self.assertNotEqual(self.model1, self.model2)


if __name__ == '__name__':
    unittest.main()

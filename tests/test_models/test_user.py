#!/usr/bin/python3
"""
adde comment here
"""
import unittest
import models.user
from datetime import datetime


class Test_User(unittest.TestCase):
    """Console methods test"""

    @classmethod
    def setUpClass(self):
        self.user1 = models.user.User()
        self.user2 = models.user.User()

    @classmethod
    def tearDownClass(self):
        del self.user1
        del self.user2

    def test_user_save_method(self):
        """tests proper functionin of save method"""

        date1 = self.user1.updated_at
        self.user1.save()
        self.assertNotEqual(self.user1.updated_at, date1)


if __name__ == '__name__':
    unittest.main()

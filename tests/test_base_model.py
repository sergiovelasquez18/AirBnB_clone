#!/usr/bin/python3
"""
adde comment here
"""
import unittest
import models


class Test_Console(unittest.TestCase):
    """Console methods test"""


def test_con_methods(self):
    """tests uncompleted console command lines"""
    self.assertEqual("show", "** class name missing **")

    self.assertEqual("show BaseModel", "** instance id missing **")

    self.assertEqual("destroy", "** class name missing **")

    self.assertEqual("destroy BaseModel", "** instance id missing **")

    self.assertEqual("update", "** class name missing **")

    self.assertEqual("update BaseModel", "** instance id missing **")

    self.assertEqual("update Caminar", "** class doesn't exist **")

if __name__ == '__name__':
    unittest.main()

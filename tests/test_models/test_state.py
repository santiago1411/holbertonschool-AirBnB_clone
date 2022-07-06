#!/usr/bin/python3

"""
unittest for user
"""

import models
import unittest
from models.base_model import BaseModel
from models import state
from models.state import State

class Test_state(unittest.TestCase):

    """"""

    def test_is_an_instance_user(self):
        """user instatiating"""
        my_state = State()
        self.assertIsInstance(my_state, State)
    
    def test_State_id(self):
        my_state = State()
        self.assertIsInstance(my_state.id, str)
        self.assertTrue(hasattr(my_state, "id"))
    
    def test_created(self):
        my_state = State()
        self.assertTrue(type(my_state.created_at), str)
        self.assertTrue(hasattr(my_state, "created_at"))
    
    def test_updated(self):
        my_state = State()
        self.assertTrue(type(my_state.updated_at), str)
        self.assertTrue(hasattr(my_state, "updated_at"))

if __name__ == "__main__":
    unittest.main()

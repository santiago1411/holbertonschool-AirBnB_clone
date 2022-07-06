#!/usr/bin/python3

"""
unittest for user
"""

import models
import unittest
from models.base_model import BaseModel
from models import review
from models.review import Review

class Test_review(unittest.TestCase):

    """"""

    def test_is_an_instance_user(self):
        """user instatiating"""
        my_review = Review()
        self.assertIsInstance(my_review, Review)
    
    def test_review_id(self):
        my_review = Review()
        self.assertIsInstance(my_review.id, str)
        self.assertTrue(hasattr(my_review, "id"))
    
    def test_created(self):
        my_review = Review()
        self.assertTrue(type(my_review.created_at), str)
        self.assertTrue(hasattr(my_review, "created_at"))
    
    def test_updated(self):
        my_review = Review()
        self.assertTrue(type(my_review.updated_at), str)
        self.assertTrue(hasattr(my_review, "updated_at"))

if __name__ == "__main__":
    unittest.main()

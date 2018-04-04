import unittest
import requests
from web.app import Expression

class IntergrationTest(unittest.TestCase):

    def test_right_expression(self):
        expression = "1 + 1"
        r = requests.post('http://localhost:5000', data = {'expression':expression})
        inserted = Expression.query.filter(text=expression).first()
        self.assertEqual(inserted.text, expression)

    # def test_wrong_expression(self):
    #     expression = "1 + a"
    #     r = requests.post('http://localhost:5000', data = {'expression':expression})
    #     inserted = Expression.query.filter(text=expression).first()
    #     self.assertEqual(inserted, None)
#!/usr/bin/python3
"""test module for the signup route"""
import unittest
import requests

class Test_Get_method(unittest.TestCase):
    """test cases for the get method"""

    url = "http://localhost:5000/api/v1/signup"

    def test_status_code(self):
        response = requests.get(Test_Get_method.url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.text != None)

    def test_post_method(self):
        """test the post method of signup"""
        user_info = {"first_name": "John", "last_name": "Mark",
                     "email": ".com", "password": "pass"}
        data = user_info
        headers = {"Content-Type": "application/json"}
        response = requests.post(Test_Get_method.url, json=data, headers=headers)
        self.assertEqual(response.status_code, 201)
    

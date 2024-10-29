import unittest

import requests

from unit_tests.utility import json_request, CALCULATE_API_URL


class TestCalculatorModalProductType(unittest.TestCase):

    def test_negative_calculate_invalid_product_type(self):
        json_data = json_request(60, 30000, 16.8, 25, product_type='0952359023')
        response = requests.post(CALCULATE_API_URL, json=json_data)
        self.assertTrue(response.status_code == 500, "Product type should exist.")

    def test_negative_calculate_invalid_product_type_empty(self):
        json_data = json_request(60, 30000, 16.8, 25, product_type='')
        response = requests.post(CALCULATE_API_URL, json=json_data)
        self.assertTrue(response.status_code == 500, "Product type should not be empty.")

    def test_negative_calculate_invalid_product_type_too_long(self):
        json_data = json_request(60, 30000, 16.8, 25, product_type='SMALL_LOAN_EE01SMALL_LOAN_EE01')
        response = requests.post(CALCULATE_API_URL, json=json_data)
        self.assertTrue(response.status_code == 500, "Product type should not be too long.")

    def test_negative_calculate_product_type_invalid_input_int(self):
        json_data = json_request(60, 30000, 16.8, 25, product_type=124)
        response = requests.post(CALCULATE_API_URL, json=json_data)
        self.assertTrue(response.status_code == 400, "Input type for product type should be a string.")

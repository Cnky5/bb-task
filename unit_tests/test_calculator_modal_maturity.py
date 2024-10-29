import unittest

import requests

from unit_tests.utility import json_request, CALCULATE_API_URL


class TestCalculatorModalMaturity(unittest.TestCase):

    def test_negative_calculate_negative_maturity(self):
        json_data = json_request(-1, 30000, 16.8, 15)
        response = requests.post(CALCULATE_API_URL, json=json_data)
        self.assertTrue(response.status_code == 500, "Input for maturity should not be negative.")

    def test_negative_calculate_zero_maturity(self):
        json_data = json_request(0, 10000, 16.8, 15)
        response = requests.post(CALCULATE_API_URL, json=json_data)
        self.assertTrue(response.status_code == 500, "Input for maturity should not be zero.")

    def test_negative_calculate_maturity_invalid_input(self):
        json_data = json_request("0", 10000, 16.8, 15)
        response = requests.post(CALCULATE_API_URL, json=json_data)
        self.assertTrue(response.status_code == 400, "Input for maturity should be a number.")

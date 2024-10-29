import unittest

import requests

from unit_tests import utility
from unit_tests.utility import json_request, CALCULATE_API_URL


class TestCalculatorModalAmount(unittest.TestCase):

    def test_negative_calculate_invalid_input(self):
        json_data = json_request(60, "123", 16.8, 15)
        response = requests.post(CALCULATE_API_URL, json=json_data)
        self.assertTrue(response.status_code == 400, "Input should be a number")

    def test_negative_calculate_negative_amount(self):
        json_data = json_request(60, -10000, 16.8, 15)
        response = requests.post(CALCULATE_API_URL, json=json_data)
        self.assertTrue(response.status_code == 500, "Input for amount should be positive.")

    def test_negative_calculate_amount_too_high(self):
        json_data = json_request(60, 99999999, 16.8, 15)
        response = requests.post(CALCULATE_API_URL, json=json_data)
        self.assertTrue(response.status_code == 400, "Input too high.")

    def test_negative_calculate_negative_zero_amount(self):
        json_data = json_request(60, 0, 16.8, 15)
        response = requests.post(CALCULATE_API_URL, json=json_data)
        self.assertTrue(response.status_code == 500, "Input for amount should not be zero.")

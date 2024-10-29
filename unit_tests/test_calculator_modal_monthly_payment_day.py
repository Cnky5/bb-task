import unittest

import requests

from unit_tests.utility import json_request, CALCULATE_API_URL


class TestCalculatorModalMonthlyPaymentDay(unittest.TestCase):

    def test_negative_calculate_payment_day_too_high(self):
        json_data = json_request(60, 30000, 16.8, 32)
        response = requests.post(CALCULATE_API_URL, json=json_data)
        self.assertTrue(response.status_code == 500, "Input for monthly payment day should not be over 31.")

    def test_negative_calculate_payment_day_zero(self):
        json_data = json_request(60, 30000, 16.8, 0)
        response = requests.post(CALCULATE_API_URL, json=json_data)
        self.assertTrue(response.status_code == 500, "Input for monthly payment day should not be zero.")

    def test_negative_calculate_payment_day_negative(self):
        json_data = json_request(60, 30000, 16.8, -1)
        response = requests.post(CALCULATE_API_URL, json=json_data)
        self.assertTrue(response.status_code == 500, "Input for monthly payment day should not be negative")

    def test_negative_calculate_payment_day_invalid_input(self):
        json_data = json_request(60, 30000, 16.8, "1")
        response = requests.post(CALCULATE_API_URL, json=json_data)
        self.assertTrue(response.status_code == 400, "Input for montly payment day should be a number.")
import unittest

import requests

from unit_tests.utility import json_request, CALCULATE_API_URL

class TestCalculatorModalInterestRate(unittest.TestCase):

    def test_calculate_zero_interest_rate(self):
        json_data = json_request(60, 10000, 0, 15)
        response = requests.post(CALCULATE_API_URL, json=json_data)
        self.assertTrue(response.ok)
        json_response = response.json()
        self.perform_assertions(json_response, 10209.4, 170.16, 3.29)

    def test_negative_calculate_interest_rate_negative(self):
        json_data = json_request(60, 10000, -16.8, 15)
        response = requests.post(CALCULATE_API_URL, json=json_data)
        self.assertTrue(response.status_code == 500, "Input for interest rate should not be negative.")

    def test_negative_calculate_interest_rate_invalid_input_int(self):
        json_data = json_request(60, 10000, "16.8", 15)
        response = requests.post(CALCULATE_API_URL, json=json_data)
        self.assertTrue(response.status_code == 400, "Input for interest rate should be a number.")

    def perform_assertions(self, json_response, expected_repayable_amount, expected_monthy_amount, expected_apr):
        self.assertEqual(json_response['totalRepayableAmount'], expected_repayable_amount)
        self.assertEqual(json_response['monthlyPayment'], expected_monthy_amount)
        self.assertEqual(json_response['apr'], expected_apr)

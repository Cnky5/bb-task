import unittest

import requests

from unit_tests import utility
from unit_tests.utility import json_request, CALCULATE_API_URL


class TestCalculatorModalFee(unittest.TestCase):

    def test_negative_calculate_negative_conclusion_fee(self):
        json_data = json_request(60, 30000, 16.8, 15, 3.49, -1)
        response = requests.post(CALCULATE_API_URL, json=json_data)
        self.assertTrue(response.status_code == 500, "Input for conclusion fee should not be negative.")

    def test_negative_calculate_negative_administration_fee(self):
        json_data = json_request(60, 30000, 16.8, 15, -3.49)
        response = requests.post(CALCULATE_API_URL, json=json_data)
        self.assertTrue(response.status_code == 500, "Input for administration fee should not be negative.")

    def test_negative_calculate_negative_administration_fee_input_string(self):
        json_data = json_request(60, 30000, 16.8, 15, "fee")
        response = requests.post(CALCULATE_API_URL, json=json_data)
        self.assertTrue(response.status_code == 400, "Input for administration fee should be a number.")

    def test_negative_calculate_negative_conclusion_fee_input_string(self):
        json_data = json_request(60, 30000, 16.8, 15, 3.49, "55")
        response = requests.post(CALCULATE_API_URL, json=json_data)
        self.assertTrue(response.status_code == 400, "Input for conclusion fee should be a number.")

    def perform_assertions(self, json_response, expected_repayable_amount, expected_monthy_amount, expected_apr):
        self.assertEqual(json_response['totalRepayableAmount'], expected_repayable_amount)
        self.assertEqual(json_response['monthlyPayment'], expected_monthy_amount)
        self.assertEqual(json_response['apr'], expected_apr)

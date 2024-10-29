import unittest
import requests

from unit_tests.utility import json_request, CALCULATE_API_URL

class TestCalculatorModalSmallLoanEE01(unittest.TestCase):

    """
    Here are positive test cases, including positive boundary cases for product type 'SMALL_LOAN_EE01'.
    With that, I assume that different product types allow for different sets of inputs and therefore would be
    in their own class.
    """

    def test_modal_calculator_sanity(self):
        json_data = json_request(60, 30000, 16.8, 25, 3.49, 600, currency='EUR', product_type='SMALL_LOAN_EE01')
        response = requests.post(CALCULATE_API_URL, json=json_data)
        self.assertTrue(response.ok)
        json_response = response.json()
        self.perform_assertions(json_response, 44911.07, 748.52, 19.79)
    
    def test_calculate_min_maturity(self):
        json_data = json_request(6, 10000, 16.8, 15)
        response = requests.post(CALCULATE_API_URL, json=json_data)
        self.assertTrue(response.ok)
        json_response = response.json()
        self.perform_assertions(json_response, 10606.81, 1767.81, 43.37)

    def test_calculate_max_maturity(self):
        json_data = json_request(120, 10000, 16.8, 15)
        response = requests.post(CALCULATE_API_URL, json=json_data)
        self.assertTrue(response.ok)
        json_response = response.json()
        self.perform_assertions(json_response, 21386.65, 177.54, 21.13)

    def test_calculate_maximum_loan(self):
        json_data = json_request(60, 30000, 16.8, 15)
        response = requests.post(CALCULATE_API_URL, json=json_data)
        self.assertTrue(response.ok)
        json_response = response.json()
        self.perform_assertions(json_response, 45328.47, 755.48, 19.75)

    def test_calculate_minimum_loan(self):
        json_data = json_request(60, 500, 16.8, 15)
        response = requests.post(CALCULATE_API_URL, json=json_data)
        self.assertTrue(response.ok)
        json_response = response.json()
        self.perform_assertions(json_response, 961.13, 16.03, 25639.72)

    def test_calculate_zero_administration_fee(self):
        json_data = json_request(60, 30000, 16.8, 15, 0)
        response = requests.post(CALCULATE_API_URL, json=json_data)
        self.assertTrue(response.ok)
        json_response = response.json()
        self.perform_assertions(json_response, 45119.07, 751.99, 19.5)

    def test_calculate_zero_conclusion_fee(self):
        json_data = json_request(60, 30000, 16.8, 15, 3.49, 0)
        response = requests.post(CALCULATE_API_URL, json=json_data)
        self.assertTrue(response.ok)
        json_response = response.json()
        self.perform_assertions(json_response, 45328.47, 755.48, 18.67)

    def perform_assertions(self, json_response, expected_repayable_amount, expected_monthy_amount, expected_apr):
        self.assertEqual(json_response['totalRepayableAmount'], expected_repayable_amount)
        self.assertEqual(json_response['monthlyPayment'], expected_monthy_amount)
        self.assertEqual(json_response['apr'], expected_apr)

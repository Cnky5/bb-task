import unittest

import requests

from unit_tests.utility import json_request, CALCULATE_API_URL


class TestCalculatorModalCurrency(unittest.TestCase):

    def test_negative_calculate_invalid_currency(self):
        json_data = json_request(60, 30000, 16.8, 25, currency='EWW')
        response = requests.post(CALCULATE_API_URL, json=json_data)
        self.assertTrue(response.status_code == 500, "Input should be a valid currency.")

    def test_negative_calculate_invalid_currency_special_char(self):
        json_data = json_request(60, 30000, 16.8, 25, currency='\\EUR')
        response = requests.post(CALCULATE_API_URL, json=json_data)
        self.assertTrue(response.status_code == 500, "Input should be a valid currency.")

    def test_calculate_currency_euros(self):
        json_data = json_request(126, 30000, 10.95, 27, currency='EUR')
        response = requests.post(CALCULATE_API_URL, json=json_data)
        self.assertTrue(response.ok)

    def test_calculate_currency_euros_lowercase(self):
        json_data = json_request(126, 30000, 10.95, 27, currency='eur')
        response = requests.post(CALCULATE_API_URL, json=json_data)
        self.assertTrue(response.ok)

    def test_calculate_currency_euros_too_short(self):
        json_data = json_request(126, 30000, 10.95, 27, currency='EU')
        response = requests.post(CALCULATE_API_URL, json=json_data)
        self.assertTrue(response.status_code == 500, "Input too short.")

    def test_calculate_currency_euros_too_long(self):
        json_data = json_request(126, 30000, 10.95, 27, currency='EURO')
        response = requests.post(CALCULATE_API_URL, json=json_data)
        self.assertTrue(response.status_code == 500, "Input too long.")

    def test_calculate_currency_euros_empty(self):
        json_data = json_request(126, 30000, 10.95, 27, currency='')
        response = requests.post(CALCULATE_API_URL, json=json_data)
        self.assertTrue(response.status_code == 500, "Input should not be empty.")

    def test_negative_calculate_invalid_input_int(self):
        json_data = json_request(60, 30000, 16.8, 25, currency=12)
        response = requests.post(CALCULATE_API_URL, json=json_data)
        self.assertTrue(response.status_code == 400, "Input should be a string.")
import http.client
import os
import unittest
from urllib.request import urlopen
from urllib.error import HTTPError
import pytest
from app import util
BASE_URL = os.environ.get("BASE_URL")
DEFAULT_TIMEOUT = 2  # in secs


@pytest.mark.api
class TestApi(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(BASE_URL, "URL no configurada")
        self.assertTrue(len(BASE_URL) > 8, "URL no configurada")

    # ===================================================================== add tests

    def test_api_add(self):
        url = f"{BASE_URL}/calc/add/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        self.assertEqual(
            util.convert_to_number(response.read().decode('utf-8')), 4, f"Error en la petición API a {url}"
        )

    def test_api_add_negative_positive(self):
        url = f"{BASE_URL}/calc/add/2/-2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        self.assertEqual(
            util.convert_to_number(response.read().decode('utf-8')), 0, f"Error en la petición API a {url}"
        )

    def test_api_add_nan(self):
        url = f"{BASE_URL}/calc/add/2/-"
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            print('The server couldn\'t fulfill the request.')
            print('Error code: ', e.code)
            self.assertEqual(
                e.code, http.client.BAD_REQUEST, f"Error en la petición API a {url}"
            )

    # ===================================================================== subtract tests

    def test_api_subtract(self):
        url = f"{BASE_URL}/calc/substract/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        self.assertEqual(
            util.convert_to_number(response.read().decode('utf-8')), 0, f"Error en la petición API a {url}"
        )

    def test_api_subtract_negative_positive(self):
        url = f"{BASE_URL}/calc/substract/2/-2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        self.assertEqual(
            util.convert_to_number(response.read().decode('utf-8')), 4, f"Error en la petición API a {url}"
        )

    def test_api_subtract_nan(self):
        url = f"{BASE_URL}/calc/substract/2/-"
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            print('The server couldn\'t fulfill the request.')
            print('Error code: ', e.code)
            self.assertEqual(
                e.code, http.client.BAD_REQUEST, f"Error en la petición API a {url}"
            )

    # ===================================================================== multiply tests

    def test_api_multiply(self):
        url = f"{BASE_URL}/calc/multiply/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        self.assertEqual(
            util.convert_to_number(response.read().decode('utf-8')), 4, f"Error en la petición API a {url}"
        )

    def test_api_multiply_negative_positive(self):
        url = f"{BASE_URL}/calc/multiply/5/-2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        self.assertEqual(
            util.convert_to_number(response.read().decode('utf-8')), -10, f"Error en la petición API a {url}"
        )

    def test_api_multiply_nan(self):
        url = f"{BASE_URL}/calc/multiply/2/-"
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            print('The server couldn\'t fulfill the request.')
            print('Error code: ', e.code)
            self.assertEqual(
                e.code, http.client.BAD_REQUEST, f"Error en la petición API a {url}"
            )

    # ===================================================================== divide tests

    def test_api_divide(self):
        url = f"{BASE_URL}/calc/divide/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        self.assertEqual(
            util.convert_to_number(response.read().decode('utf-8')), 1, f"Error en la petición API a {url}"
        )

    def test_api_divide_negative_positive(self):
        url = f"{BASE_URL}/calc/divide/10/-2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        self.assertEqual(
            util.convert_to_number(response.read().decode('utf-8')), -5, f"Error en la petición API a {url}"
        )

    def test_api_divide_nan(self):
        url = f"{BASE_URL}/calc/divide/2/-"
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            print('The server couldn\'t fulfill the request.')
            print('Error code: ', e.code)
            self.assertEqual(
                e.code, http.client.BAD_REQUEST, f"Error en la petición API a {url}"
            )

    def test_api_divide_by_zero(self):
        url = f"{BASE_URL}/calc/divide/2/0"
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            print('The server couldn\'t fulfill the request.')
            print('Error code: ', e.code)
            self.assertEqual(
                e.code, http.client.BAD_REQUEST, f"Error en la petición API a {url}"
            )
    
    # ===================================================================== power tests

    def test_api_power(self):
        url = f"{BASE_URL}/calc/power/2/3"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        self.assertEqual(
            util.convert_to_number(response.read().decode('utf-8')), 8, f"Error en la petición API a {url}"
        )

    def test_api_power_negative_positive(self):
        url = f"{BASE_URL}/calc/power/2/-2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        self.assertEqual(
            util.convert_to_number(response.read().decode('utf-8')), 0.25, f"Error en la petición API a {url}"
        )

    def test_api_power_nan(self):
        url = f"{BASE_URL}/calc/power/2/-"
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            print('The server couldn\'t fulfill the request.')
            print('Error code: ', e.code)
            self.assertEqual(
                e.code, http.client.BAD_REQUEST, f"Error en la petición API a {url}"
            )

    def test_api_power_nan2(self):
        url = f"{BASE_URL}/calc/power/u/2"
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            print('The server couldn\'t fulfill the request.')
            print('Error code: ', e.code)
            self.assertEqual(
                e.code, http.client.BAD_REQUEST, f"Error en la petición API a {url}"
            )
    
    # ===================================================================== square root tests

    def test_api_sqrt(self):
        url = f"{BASE_URL}/calc/sqrt/9"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        self.assertEqual(
            util.convert_to_number(response.read().decode('utf-8')), 3, f"Error en la petición API a {url}"
        )

    def test_api_sqrt(self):
        url = f"{BASE_URL}/calc/sqrt/4"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        self.assertEqual(
            util.convert_to_number(response.read().decode('utf-8')), 2, f"Error en la petición API a {url}"
        )
    
    def test_api_sqrt_floating_point(self):
        url = f"{BASE_URL}/calc/sqrt/0.25"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        self.assertEqual(
            util.convert_to_number(response.read().decode('utf-8')), 0.5, f"Error en la petición API a {url}"
        )

    def test_api_sqrt_nan(self):
        url = f"{BASE_URL}/calc/sqrt/u"
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            print('The server couldn\'t fulfill the request.')
            print('Error code: ', e.code)
            self.assertEqual(
                e.code, http.client.BAD_REQUEST, f"Error en la petición API a {url}"
            )

    def test_api_sqrt_math_error(self):
        url = f"{BASE_URL}/calc/sqrt/-10"
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            print('The server couldn\'t fulfill the request.')
            print('Error code: ', e.code)
            self.assertEqual(
                e.code, http.client.BAD_REQUEST, f"Error en la petición API a {url}"
            )

    # ===================================================================== log10 tests

    def test_api_log10(self):
        url = f"{BASE_URL}/calc/log10/100"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        self.assertEqual(
            util.convert_to_number(response.read().decode('utf-8')), 2, f"Error en la petición API a {url}"
        )
    
    def test_api_log10_floating_point(self):
        url = f"{BASE_URL}/calc/log10/0.1"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        self.assertEqual(
            util.convert_to_number(response.read().decode('utf-8')), -1, f"Error en la petición API a {url}"
        )

    def test_api_log10_math_error(self):
        url = f"{BASE_URL}/calc/log10/-10"
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            print('The server couldn\'t fulfill the request.')
            print('Error code: ', e.code)
            self.assertEqual(
                e.code, http.client.BAD_REQUEST, f"Error en la petición API a {url}"
            )

    def test_api_log10_nan(self):
        url = f"{BASE_URL}/calc/log10/o"
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            print('The server couldn\'t fulfill the request.')
            print('Error code: ', e.code)
            self.assertEqual(
                e.code, http.client.BAD_REQUEST, f"Error en la petición API a {url}"
            )

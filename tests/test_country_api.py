import unittest
from unittest.mock import patch
from API.country_api import (get_country_info, get_country_flag, get_country_details)


class TestCountryAPI(unittest.TestCase):

    @patch("API.country_api.requests.get")
    def test_get_country_info(self, mock_get): # Mocks the requests.get method to simulate an API response for retrieving country information.

        mock_get.return_value.status_code = 200 # Simulates a successful API response with a status code of 200.
        mock_get.return_value.json.return_value = [
            {"name": {"common": "Germany"}}
        ]

        result = get_country_info("Germany")

        self.assertEqual(result[0]["name"]["common"], "Germany")

    @patch("API.country_api.requests.get")
    def test_get_country_flag(self, mock_get):

        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [
            {
                "flags": {
                    "png": "flag_url"
                }
            }
        ]

        result = get_country_flag("Germany")

        self.assertEqual(result, "flag_url")

    @patch("API.country_api.requests.get")
    def test_get_country_details(self, mock_get):

        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [
            {
                "name": {"common": "Germany"},
                "capital": ["Berlin"],
                "region": "Europe",
                "flags": {"png": "flag_url"},
                "population": 80000000,
                "area": 357000
            }
        ]

        result = get_country_details("Germany")

        self.assertEqual(result["name"], "Germany")
        self.assertEqual(result["capital"], "Berlin")
        self.assertEqual(result["region"], "Europe")


if __name__ == "__main__":
    unittest.main()
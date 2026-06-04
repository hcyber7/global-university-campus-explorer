import unittest
from unittest.mock import patch

from API.Geocoding_services import (
    get_location,
    get_country_center
)


class TestGeocoding(unittest.TestCase):

    @patch("API.Geocoding_services.requests.get")
    def test_get_location(self, mock_get):

        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "results": [
                {
                    "latitude": 52.5200,
                    "longitude": 13.4050
                }
            ]
        }

        result = get_location("Berlin")

        self.assertEqual(result, (52.52, 13.405))

    @patch("API.Geocoding_services.requests.get")
    def test_get_country_center(self, mock_get):

        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "results": [
                {
                    "latitude": 51.1657,
                    "longitude": 10.4515
                }
            ]
        }

        result = get_country_center("Germany")

        self.assertEqual(result, (51.1657, 10.4515))


if __name__ == "__main__":
    unittest.main()
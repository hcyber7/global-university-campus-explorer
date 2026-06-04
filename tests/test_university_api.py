import unittest
from unittest.mock import patch

from API.University_api import (
    search_universities,
    search_universities_by_name
)


class TestUniversityAPI(unittest.TestCase):

    @patch("API.University_api.requests.get")
    def test_search_universities(self, mock_get):

        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [
            {"name": "University of Munich"}
        ]

        result = search_universities("Germany")

        self.assertEqual(result[0]["name"], "University of Munich")

    @patch("API.University_api.requests.get")
    def test_search_universities_by_name(self, mock_get):

        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [
            {"name": "Harvard University"}
        ]

        result = search_universities_by_name("Harvard")

        self.assertEqual(result[0]["name"], "Harvard University")


if __name__ == "__main__":
    unittest.main()
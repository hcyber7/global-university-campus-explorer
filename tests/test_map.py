import unittest
from unittest.mock import patch

from maps.map import create_country_map


class TestMap(unittest.TestCase):

    @patch("maps.map.get_location")
    def test_create_country_map(self, mock_location):

        mock_location.return_value = (52.52, 13.40)

        result = create_country_map("Germany")

        self.assertEqual(result, True)


if __name__ == "__main__":
    unittest.main()
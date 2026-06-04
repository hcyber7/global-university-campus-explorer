import unittest

from Database.database import (
    add_to_favorites,
    get_favorites,
    clear_all_favorites
)


class TestDatabase(unittest.TestCase):

    def test_add_and_get_favorites(self):

        clear_all_favorites()

        add_to_favorites(
            "Harvard University",
            "United States",
            "https://harvard.edu"
        )

        favorites = get_favorites()

        self.assertEqual(favorites[0]["name"], "Harvard University")

    def test_clear_favorites(self):

        add_to_favorites(
            "Test University",
            "Germany",
            "https://test.com"
        )

        clear_all_favorites()

        favorites = get_favorites()

        self.assertEqual(favorites, [])


if __name__ == "__main__":
    unittest.main()
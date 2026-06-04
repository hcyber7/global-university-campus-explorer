import unittest

from charts.chart import (
    create_country_distribution_chart,
    create_stats_chart
)

class TestChart(unittest.TestCase): 

    def test_country_distribution(self):

        universities = [
            {"country": "Germany"},
            {"country": "Germany"},
            {"country": "France"}
        ]

        result = create_country_distribution_chart(universities) 

        self.assertEqual(result[0]["country"], "Germany")
        self.assertEqual(result[0]["count"], 2)

    def test_empty_distribution(self):

        result = create_country_distribution_chart([])

        self.assertEqual(result, [])

    def test_stats_chart(self):

        stats = {
            "total_searches": 10,
            "total_favorites": 5,
            "unique_countries": 3
        }

        result = create_stats_chart(stats)

        self.assertEqual(result["searches"], 10)
        self.assertEqual(result["favorites"], 5)
        self.assertEqual(result["countries"], 3)


if __name__ == "__main__":
    unittest.main()
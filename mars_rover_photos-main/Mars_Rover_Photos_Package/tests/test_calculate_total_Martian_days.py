import unittest
from datetime import datetime
from src.calculate_total_sols import calculate_total_sols  

class TestCalculateTotalSols(unittest.TestCase):
    def test_valid_dates(self):
        landing_date = '2022-01-01'
        launch_date = '2021-01-01'

    
        result = calculate_total_sols(landing_date, launch_date)

        # Assertions
        self.assertIsNotNone(result)
        self.assertEqual(result, 365)  # Assuming a one-year difference

    def test_invalid_dates(self):
        # Test case with invalid dates
        landing_date = 'invalid_date'
        launch_date = '2021-01-01'

        # Call the function with test parameters
        result = calculate_total_sols(landing_date, launch_date)

        # Assertions
        self.assertIsNone(result)
        self.assertRegex(str(result), 'Date parsing error')

if __name__ == '__main__':
    unittest.main()

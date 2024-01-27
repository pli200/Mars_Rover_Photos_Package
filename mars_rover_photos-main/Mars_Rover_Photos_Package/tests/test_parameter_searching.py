import unittest
from unittest.mock import patch, Mock
from src.get_mars_rover_photos import get_mars_rover_photos  

class TestGetMarsRoverPhotos(unittest.TestCase):
    @patch('src.get_mars_rover_photos')  
    def test_successful_request(self, mock_get):
        # Set up the mock response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'photos': [{'id': 1, 'camera': {'name': 'FHAZ'}}]}  
        mock_get.return_value = mock_response

     
        result = get_mars_rover_photos(sol=1000, api_key='DEMO_KEY')  

        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 1)

    @patch('src.get_mars_rover_photos.requests.get')
    def test_failed_request(self, mock_get):
        # Set up the mock response for a failed request
        mock_response = Mock()
        mock_response.status_code = 404
        mock_response.text = 'Not Found'
        mock_get.return_value = mock_response

        # Call the function with test parameters
        result = get_mars_rover_photos(sol=1000, api_key='DEMO_KEY')  

        # Assertions
        self.assertIsNone(result)
        print.assert_called_once_with("Error: 404 - Not Found")

if __name__ == '__main__':
    unittest.main()

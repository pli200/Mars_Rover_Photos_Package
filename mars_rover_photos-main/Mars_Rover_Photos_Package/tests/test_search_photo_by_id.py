import unittest
from unittest.mock import patch, Mock
from src.search_photo_by_id import search_photo_by_id  
class TestSearchPhotoById(unittest.TestCase):
    @patch('src.search_photo_by_id.requests.get')  
    def test_existing_photo(self, mock_get):
        # Test case for an existing photo
        photo_id = 123
        api_key = 'YOUR_API_KEY'
        
        # Set up the mock response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'photo': {'id': 456, 'camera': {'name': 'FHAZ'}}}  
        mock_get.return_value = mock_response

        # Call the function with test parameters
        result = search_photo_by_id(photo_id, api_key)

        # Assertions
        self.assertIsNotNone(result)
        self.assertEqual(result['id'], photo_id)

    @patch('src.search_photo_by_id.requests.get')  
    def test_nonexistent_photo(self, mock_get):
        # Test case for a nonexistent photo
        photo_id = 456
        api_key = 'YOUR_API_KEY'
        
        # Set up the mock response
        mock_response = Mock()
        mock_response.status_code = 404
        mock_response.text = 'Not Found'
        mock_get.return_value = mock_response

        # Call the function with test parameters
        result = search_photo_by_id(photo_id, api_key)

        # Assertions
        self.assertIsNone(result)
        print.assert_called_once_with(f"Photo with ID {photo_id} not found.")

    @patch('your_module.requests.get')  # Replace 'your_module' with the actual module name
    def test_error_response(self, mock_get):
        # Test case for an error response
        photo_id = 789
        api_key = 'YOUR_API_KEY'
        
        # Set up the mock response for an error
        mock_response = Mock()
        mock_response.status_code = 500
        mock_response.text = 'Internal Server Error'
        mock_get.return_value = mock_response

        # Call the function with test parameters
        result = search_photo_by_id(photo_id, api_key)

        # Assertions
        self.assertIsNone(result)
        print.assert_called_once_with(f"Error: 500 - Internal Server Error")

if __name__ == '__main__':
    unittest.main()

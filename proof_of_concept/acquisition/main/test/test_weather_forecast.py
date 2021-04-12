import unittest
import sys
sys.path.insert(0, '..')

from weather_forecast import get_openweather_api_response

class ResponseTestCase(unittest.TestCase):

   def test_response(self):
       response = get_openweather_api_response(45.309812,18.41042,"550617cb3af649e1d6729a3f78b24e17")
       # keyword "hourly" must be in the response
       self.assertIn('hourly', response)
       # keyword "cod" must not be in the response: it indicades the error code
       self.assertNotIn('cod', response)
       # results must be exactly 48 (hours)
       self.assertEqual(len(response['hourly']) , 48)

unittest.main()

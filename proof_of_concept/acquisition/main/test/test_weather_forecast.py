import unittest
import sys
sys.path.insert(0, '..')

from weather_forecast import get_onecall_api_response

class ResponseTestCase(unittest.TestCase):

   def test_response(self):
       response = get_onecall_api_response(45.309812,18.41042,"550617cb3af649e1d6729a3f78b24e17")
       # results must contain 48 hourly_forecast)
       self.assertEqual(len(response['hourly']) , 48)

unittest.main()

import os
import unittest
import sys
sys.path.insert(0, '..')

from detect import fetch_read_m3u8

class ResponseTestCase(unittest.TestCase):

   def test_fetch_read_m3u8(self):
       mock_link = "https://cdn-004.whatsupcams.com/hls/hr_novska01.m3u8"
       mock_prefix = "https://cdn-004.whatsupcams.com/hls/"
       response = fetch_read_m3u8(mock_link, mock_prefix)
       # results must contain 48 hourly_forecast)
       self.assertIn(mock_prefix, response)
       self.assertIn(".ts", response)
       print(response)


unittest.main()

import os
import unittest
import sys
import cv2
import numpy
sys.path.insert(0, '..')

from detect import fetch_read_m3u8, extract_frame_from_video_url

class ResponseTestCase(unittest.TestCase):

   def test_fetch_read_m3u8(self):
       mock_link = "https://cdn-004.whatsupcams.com/hls/hr_novska01.m3u8"
       mock_prefix = "https://cdn-004.whatsupcams.com/hls/"
       response = fetch_read_m3u8(mock_link, mock_prefix)
       print(response)
       # results must contain 48 hourly_forecast)
       self.assertIn(mock_prefix, response)
       self.assertIn(".ts", response)
       

   def test_extract_frame_from_video_url(self):
       mock_link = "samples/hr_novska01-51104.ts"
       response, frame = extract_frame_from_video_url(mock_link)
       sample = cv2.imread("samples/frame_novska.jpg")

       numpy.testing.assert_array_almost_equal(sample, frame,decimal=-2)


unittest.main()

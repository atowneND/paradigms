import unittest
import requests
import json

class TestReset(unittest.TestCase):

    SITE_URL = 'http://student02.cse.nd.edu:40092'
    RESET_URL = SITE_URL + '/reset/'

    def test_reset_data(self):
        m = {}
        m['apikey'] = '1O44fU28eQ'
        r = requests.put(self.RESET_URL)

if __name__ == "__main__":
    unittest.main()


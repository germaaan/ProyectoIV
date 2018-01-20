import unittest
import json
import requests


def test_cve():
	r = requests.get('http://basecve.westeurope.cloudapp.azure.com/api/search/internet-explorer/8')
	return r.status_code == requests.codes.ok


class TestTravisCVE(unittest.TestCase):
    def testCVE(self):
        self.assertTrue(test_cve())


if __name__ == '__main__':
    unittest.main()

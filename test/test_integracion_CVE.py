import unittest
import json
import requests


def test_cve():
	r = requests.get('http://basecve.westeurope.cloudapp.azure.com/api/search/internet-explorer/8')
	return r.status_code == requests.codes.ok

def test_is_up():
	r = requests.get('http://basecve.westeurope.cloudapp.azure.com/status')
	return r.status_code == requests.codes.ok

def test_not_valid():
	r = requests.get('http://basecve.westeurope.cloudapp.azure.com/end-point-not-valid')
	return r.status_code == 404

class TestTravisCVE(unittest.TestCase):
    def testCVE(self):
		self.assertTrue(test_cve())
		self.assertTrue(test_is_up())
		self.assertTrue(test_not_valid())


if __name__ == '__main__':
    unittest.main()

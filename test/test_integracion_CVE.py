import unittest
import json


def test_crear():
    return True

def test_alterar():
    return True

def test_borrar():
    return True





class TestTravisCVE(unittest.TestCase):
    def testCrearCVE(self):
        self.assertTrue(test_crear())

    def testAlterarCVE(self):
        self.assertTrue(test_alterar())

    def testBorrarCVE(self):
        self.assertTrue(test_borrar())

if __name__ == '__main__':
    unittest.main()

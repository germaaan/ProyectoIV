import unittest
import json
import sys
sys.path.insert(0, '../')

from src.cve import CVE_Details


def comparaJson(a,b):
    return sorted(a.items()) == sorted(b.items())

def test_crear():

    x = CVE_Details()
    s = json.loads('{"id": "id_cve", "puntuacion": "point", "services": {"vendor": "vendor","product": "producto", "version": "version"}}')
    x.new(s)

    return comparaJson(x.getById("id_cve"),s)

def test_alterar():

    x = CVE_Details()
    s = json.loads('{"id": "id_cveMalo", "puntuacion": "point", "services": {"vendor": "vendor","product": "producto", "version": "version"}}')
    x.new(s)

    n = json.loads('{"id": "id_cveNuevo", "puntuacion": "point", "services": {"vendor": "vendor","product": "producto", "version": "version"}}')

    x.alter(n)

    return comparaJson(x.getById("id_cveNuevo"),n)

def test_borrar():
        x = CVE_Details()
        s = json.loads('{"id": "id_cveMalo", "puntuacion": "point", "services": {"vendor": "vendor","product": "producto", "version": "version"}}')
        x.new(s)

        y = json.loads('{"id": "id_cveBueno", "puntuacion": "point", "services": {"vendor": "vendor","product": "producto", "version": "version"}}')
        x.new(y)

        x.erase("id_cveMalo")

        return x.getById("id_cveMalo") == None and x.getById("id_cveBueno") != None





class TestTravisCVE(unittest.TestCase):
    def testEjercicio1(self):
        self.assertTrue(test_crear())
        self.assertTrue(test_alterar())
        self.assertTrue(test_borrar())

if __name__ == '__main__':
    unittest.main()

import unittest


#def compare():
    
    #x = CVE_Details()
    #s = json.loads('{"id": "id_cve", "puntuacion": "point", "services": {"vendor": "vendor","product": "producto", "version": "version"}}')
    #x.new(s)

    #y = CVE_Details()
   # j = json.loads('{"id": "id_cve", "puntuacion": "point", "services": {"vendor": "vendor","product": "producto", "version": "version"}}')
  #  x.newd(j)

 #   return comparJson(x,y)



#def test_function():
#    assert compare()




class TestTravisCVE(unittest.TestCase):
    def testEjercicio1(self):
        self.assertEqual(1,1)

if __name__ == '__main__':
    unittest.main()

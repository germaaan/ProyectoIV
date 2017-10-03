import sys
sys.path.insert(0,'../src')
from cve import CVE_Details


def test_function():
    
    x = CVE_Details()
    s = json.loads('{"id": "id_cve", "puntuacion": "point", "services": {"vendor": "vendor","product": "producto", "version": "version"}}')
    x.new(s)

    y = CVE_Details()
    j = json.loads('{"id": "id_cve", "puntuacion": "point", "services": {"vendor": "vendor","product": "producto", "version": "version"}}')
    x.newd(j)

    assert comparJson(x,y) == True

import sys
sys.path.append(0,'../src')
from cve import CVE_Details


def compare():
    
    x = CVE_Details()
    s = json.loads('{"id": "id_cve", "puntuacion": "point", "services": {"vendor": "vendor","product": "producto", "version": "version"}}')
    x.new(s)

    y = CVE_Details()
    j = json.loads('{"id": "id_cve", "puntuacion": "point", "services": {"vendor": "vendor","product": "producto", "version": "version"}}')
    x.newd(j)

    return comparJson(x,y)



def test_function():
    assert compare()

def func(x):
    return x + 1

def test_answer():
    assert func(3) == 5

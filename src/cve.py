import json


def compareJson(a,b):
    return sorted(a.items()) == sorted(b.items())


class CVE_Details():

    #Datos a almacenar idCVE, version_afectada, nivel, enlace
    # json => {"id": "id_cve", "puntuacion": "point", "services": {"vendor": "vendor","product": "producto", "version": "version"}}

    def __init__(self):
        self.data = {}

    def new(self,nuevo):
        self.data[nuevo["id"]] = nuevo
        #print(self.data)

    def alter(self,alter):
        self.data[alter["id"]] = nuevo
        #print(self.data)

    def eraseById(self,erase):
        del self.data[erase["id"]]
        #print(self.data)

    def erase(self,id):
        del self.data[id]
        #print(self.data)

    def getById(self,data):
        return self.data[data]

    

if __name__ == '__main__':

    x = CVE_Details()
    js = json.loads('{"id": "id_cve", "puntuacion": "point", "services": {"vendor": "vendor","product": "producto", "version": "version"}}')
    x.new(js)
    x.erase("id_cve")

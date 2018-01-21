from fabric.api import sudo,run

#Metodo que clona, instala python3 y los requisitos de mi proyecto
def installcve():
	run('git clone https://github.com/ainokila/ProyectoIV')
	run('sudo apt-get update')
	run('sudo apt-get -y install build-essential python3-setuptools build-essential libssl-dev libffi-dev python-dev')
	run('cd ProyectoIV/ && pip3 install -r requirements.txt')

#Borra el directorio de mi proyecto
def removecve():
	run('sudo rm -rf ./ProyectoIV')

#Arranca gunicorn indicandole la ruta de mi app y el puerto, se pone con sudo ya que si el puerto es menor de 1024, siempre usa sudo.
def startcve():
	run('cd ~/ProyectoIV/ && sudo gunicorn -b 0.0.0.0:80 app:app --log-file=- &')

	

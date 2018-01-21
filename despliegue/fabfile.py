from fabric.api import sudo,run
import os


def installcve():
	run('git clone https://github.com/ainokila/ProyectoIV')
	run('sudo apt-get update')
	run('sudo apt-get -y install build-essential python3-setuptools build-essential libssl-dev libffi-dev python-dev')
	run('cd ProyectoIV/ && pip3 install -r requirements.txt')

def removecve():
	run('sudo rm -rf ./ProyectoIV')

def startcve():
	run('cd ~/ProyectoIV/ && sudo gunicorn -b 0.0.0.0:80 app:app --log-file=- &')

	

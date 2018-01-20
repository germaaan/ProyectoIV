# coding: utf-8

from fabric.api import sudo, cd, env, run, shell_env
import os


def installcve():
	run('git clone https://github.com/ainokila/ProyectoIV')
	run('sudo apt-get update')
	run('sudo apt-get -y install python3-setuptools')
	run('sudo apt-get -y install python3-dev')
	run('sudo apt-get -y install build-essential')
	run('sudo apt-get -y install python3-psycopg2')
	run('sudo apt-get -y install libpq-dev')
	run('sudo apt-get -y install python3-pip')
	run('cd ProyectoIV/ && pip3 install -r requirements.txt')

def removecve():
	run('sudo rm -rf ./ProyectoIV')

def startcve():
	run('cd ~/ProyectoIV/ && gunicorn app:app --log-file=- &')
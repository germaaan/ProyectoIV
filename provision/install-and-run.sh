#!/bin/bash

vagrant up --provider=azure

fab -f ../despliegue/fabfile.py -H vagrant@basecve.westeurope.cloudapp.azure.com removecve
fab -f ../despliegue/fabfile.py -H vagrant@basecve.westeurope.cloudapp.azure.com installcve
fab -f ../despliegue/fabfile.py -H vagrant@basecve.westeurope.cloudapp.azure.com startcve
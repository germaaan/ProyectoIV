[![Build Status](https://travis-ci.org/ainokila/ProyectoIV.svg?branch=master)](https://travis-ci.org/ainokila/ProyectoIV)

# Información del proyecto
## Descripción del proyecto

Este proyecto va a consitir en un servicio en el cual hay una serie de vulnerabilidades conocidas y reconocidas, por lo que un usuario registrado podra pasarle los datos que quiere comprobar y se le devolvera otros datos, una vez que se haya comparado con la base de datos. La base de datos se rellenará a partir de otra que es pública. La finalidad es pasarle un listado de servicios instalados en una maquina, el servicio los analiza y lo compara con la base de datos, los datos devueltos serán de utilidad para arreglar deficiencias.

## Servicios necesarios

    Lenguaje: Python 3.4
    Base datos: MongoDB
    Test de integración: TravisCI


Repositorio para el proyecto de la asignatura Infrastructura Virtual 2017-2018.

## Despliegue en PaaS

Para este proyecto utilizaré el paas de Heroku, en los que para poder desplegarlo he seguido los siguientes pasos:

1. Dar de alta en la web de [Heroku](https://dashboard.heroku.com/login)
2. Instalar toolbelt de Heroku

    `wget -qO- https://cli-assets.heroku.com/install-ubuntu.sh | sh`

3. Iniciamos sesión en heroku

    `heroku login`

4. Creamos el fichero runtime.txt, indicando la versión de python ejecutará la aplicación.
5. Creamos el fichero Procfile, donde indicamos como arranca nuestra aplicación.
6. Creamos la aplicación de Heroku

    `heroku create`

7. Añadimos la base de datos mongoDB de mlab a la aplicación anterior.
8. Subimos la aplicación a Heroku

    `git push heroku master`

Despliegue https://frozen-everglades-36730.herokuapp.com/



## Despliegue en contenedor

1. Darse de alta en zeit
2. Instalar now
3. Subir el proyecto con el Dockerfile

También para reducir el proceso y se puede realizar con

	docker pull ainokila/iv

https://hub.docker.com/r/ainokila/proyectoiv/~/dockerfile/

De esta manera ya se podrá desplegar el contenedor personalizado.

Contenedor: https://proyectoiv-rkuypdqhfx.now.sh


## Despliegue en maquina virtual - Azure

1. Darse de alta usando el cupón proporcionado por el profesor.
2. Obtener las claves para poder acceder a traves de keys.
3. Exportar las claves a nuestro ordenador para que se puedan utilizar a través de Vagrant.
3. Crear la maquina virtual y provisionarla con ansible usando:

	`vagrant up --provider=azure`

4. Si queremos que todo el proceso se haga de manera automatica debemos usar:


	`vagrant up --provider=azure`
	`fab -f ./despliegue/fabfile.py -H vagrant@basecve.westeurope.cloudapp.azure.com removecve`
	`fab -f ./despliegue/fabfile.py -H vagrant@basecve.westeurope.cloudapp.azure.com installcve`
	`fab -f ./despliegue/fabfile.py -H vagrant@basecve.westeurope.cloudapp.azure.com startcve`

5. Después de esperar ya tendremos nuestro sistema funcionando en produción.

Despliegue final: basecve.westeurope.cloudapp.azure.com

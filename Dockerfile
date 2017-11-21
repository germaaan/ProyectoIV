FROM ubuntu:16.04
MAINTAINER ainokila

# Configuracion del entorno
RUN apt-get update
RUN apt-get install -y python-setuptools
RUN apt-get install -y python-dev
RUN apt-get install -y build-essential
RUN apt-get install -y libpq-dev
RUN apt-get install -y python-pip
RUN pip install --upgrade
RUN apt-get install net-tools

# Instalación
RUN apt-get install -y git
RUN git clone https://github.com/ainokila/ProyectoIV
# Instalación de las dependecncias del proyecto
RUN pip install -r ProyectoIV/requirements.txt
EXPOSE 8000
CMD cd ProyectoIV && python3 app.py

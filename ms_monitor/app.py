import requests
import json
import time
from flask import Flask
import logging


url = "http://localhost:5001/ping"
response = None
app = Flask("Monitor Ping-Echo")
logging.basicConfig(filename='monitor.log', level=logging.DEBUG, format='%(name)s - %(levelname)s - %(message)s')

for i in range(0, 100):
    try:
        response = requests.get(url)
        status = response.status_code

        if status == 200:
            app.logger.info("Microservicio paciente disponible.")
        else:

            app.logger.critical("Microservicio paciente disponible, pero alguna dependencia no esta disponible.")
    except requests.exceptions.RequestException:
        app.logger.critical("Microservicio paciente no disponible")


    time.sleep(3)
    i=i+1

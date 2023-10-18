import json
from json import JSONDecodeError

import requests
import os
from dotenv import load_dotenv #pip install python-dotenv

class Weather():

    def __init__(self):
        load_dotenv()
        
        self.__url = str(os.getenv('URL_WEATHER') + ':8086/api/EPOC/information')
                         

    def sent_information(self, **kwargs):
        endpoint =  self.__url
        
        headers = {
            "Content-Type": "application/json"
        }

        response = requests.post(endpoint, headers=headers, data=json.dumps(kwargs["coordenadas"]))
        if response.status_code == 200:
            try:
                data = response.json()
                return data
            except json.decoder.JSONDecodeError as e:
                return str(f'Weather Error {e}')  


# Esteban Andres Ramirez Gonzalez
# Inacap Ingenieria en informatica - Vespertino
# Programación Orientada a Objeto Seguro (TI3V21/V-IEI-N2-P3-C1/V Puente Alto IEI)

import requests

class CurrencyService():
    def __init__(self):
        self.api_url = "https://mindicador.cl/api/dolar"

    def obtenerValorDolar(self):
        try:

            response = requests.get(self.api_url)
            response.raise_for_status()
            data = response.json()

            dolar = data['serie'][0]['valor']
            return dolar


        except (requests.RequestException, KeyError) as ex:
            print(f"Error al obtener el valor del dolar {ex}")
            return 1
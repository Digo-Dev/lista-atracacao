import json
from datetime import datetime, timedelta
import requests
import pandas as pd

def autenticarTecon():
    credenciais = {
        "usuario": "BRASTS",
        "senha": "bra2202",
        "unidade": "Tecon_Santos"
    }

    urlAuth = 'https://integraaquiapi.santosbrasil.com.br/autenticar'
    token = requests.post(urlAuth, json=credenciais)
    if(token.ok != True):
        print('Falha ao logar! verifique Login e senha do te')
    else:
        auth = token.json()['access_token']
        return auth

def recuperarListaTecon():
    codigo = autenticarTecon()
    urlLista = 'https://integraaquiapi.santosbrasil.com.br/listaAtracacao/listaAtracacao'
    periodo = {
        "inicioLista": f"{datetime.today-timedelta(days=5)}",
        "fimLista": f"{datetime.today+timedelta(days=50)}"
    }
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {codigo}'
        }
    ListaTecon = requests.post(urlLista, headers=headers, json=periodo)
    for i in range(2):
        if (ListaTecon.ok != True):
            print('Token desatualizado, realizando nova autenticação')
            codigo = autenticarTecon()
            print("Não foi possivel autenticar!")
        else:
            return ListaTecon
    return 'Lista Tecon não recuperada'

lista = recuperarListaTecon().json()
print(lista)
pd.DataFrame.from_records(lista)

from google.colab import auth
auth.authenticate_user()

import gspread
from google.auth import default
creds, _ = default()

gc = gspread.authorize(creds)

worksheet = gc.open_by_key('1VAUogRrVF0ucx9xYPv5L8ZGGhodsIhEbR0aNmAh-Ci0')

# get_all_values gives a list of rows.
rows = worksheet.get_worksheet(0).
print(rows)

# Convert to a DataFrame and render.
import pandas as pd
pd.DataFrame.from_records(rows)